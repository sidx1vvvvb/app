from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
import logging
from ..models.Review import Review, ReviewCreate, ReviewUpdate
from ..database import db

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/reviews", tags=["reviews"])

@router.get("/", response_model=List[Review])
async def get_reviews(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=50),
    featured: Optional[bool] = None,
    product_id: Optional[str] = None
):
    """Get reviews with optional filtering"""
    try:
        query = {}
        if featured is not None:
            query["featured"] = featured
        if product_id:
            query["product_id"] = product_id
        
        cursor = db.reviews.find(query).sort("created_at", -1).skip(skip).limit(limit)
        reviews = await cursor.to_list(length=limit)
        
        return [Review(**review) for review in reviews]
    except Exception as e:
        logger.error(f"Error fetching reviews: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/featured", response_model=List[Review])
async def get_featured_reviews(limit: int = Query(3, ge=1, le=10)):
    """Get featured testimonials for homepage"""
    try:
        cursor = db.reviews.find({"featured": True}).sort("created_at", -1).limit(limit)
        reviews = await cursor.to_list(length=limit)
        
        return [Review(**review) for review in reviews]
    except Exception as e:
        logger.error(f"Error fetching featured reviews: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/product/{product_id}", response_model=List[Review])
async def get_product_reviews(
    product_id: str,
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=50)
):
    """Get reviews for a specific product"""
    try:
        cursor = db.reviews.find({"product_id": product_id}).sort("created_at", -1).skip(skip).limit(limit)
        reviews = await cursor.to_list(length=limit)
        
        return [Review(**review) for review in reviews]
    except Exception as e:
        logger.error(f"Error fetching product reviews: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/", response_model=Review)
async def create_review(review: ReviewCreate):
    """Submit a new review"""
    try:
        review_dict = review.dict()
        new_review = Review(**review_dict)
        
        await db.reviews.insert_one(new_review.dict())
        
        # Update product rating if it's a product review
        if review.product_id:
            await update_product_rating(review.product_id)
        
        logger.info(f"New review submitted for product {review.product_id}")
        return new_review
    except Exception as e:
        logger.error(f"Error creating review: {e}")
        raise HTTPException(status_code=500, detail="Failed to submit review")

@router.put("/{review_id}", response_model=Review)
async def update_review(review_id: str, review_update: ReviewUpdate):
    """Update a review (admin endpoint)"""
    try:
        # Check if review exists
        existing_review = await db.reviews.find_one({"id": review_id})
        if not existing_review:
            raise HTTPException(status_code=404, detail="Review not found")
        
        # Update review
        update_dict = {k: v for k, v in review_update.dict().items() if v is not None}
        if update_dict:
            await db.reviews.update_one(
                {"id": review_id},
                {"$set": update_dict}
            )
        
        # Return updated review
        updated_review = await db.reviews.find_one({"id": review_id})
        return Review(**updated_review)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating review {review_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

async def update_product_rating(product_id: str):
    """Update product rating based on reviews"""
    try:
        # Calculate average rating
        pipeline = [
            {"$match": {"product_id": product_id}},
            {"$group": {
                "_id": None,
                "avg_rating": {"$avg": "$rating"},
                "review_count": {"$sum": 1}
            }}
        ]
        
        result = await db.reviews.aggregate(pipeline).to_list(1)
        
        if result:
            avg_rating = round(result[0]["avg_rating"], 1)
            review_count = result[0]["review_count"]
            
            # Update product
            await db.products.update_one(
                {"id": product_id},
                {"$set": {"rating": avg_rating, "review_count": review_count}}
            )
    except Exception as e:
        logger.error(f"Error updating product rating: {e}")