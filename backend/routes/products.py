from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
import logging
from models.Product import Product, ProductCreate, ProductUpdate
from database import db

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=List[Product])
async def get_products(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    category: Optional[str] = None,
    featured: Optional[bool] = None,
    search: Optional[str] = None
):
    """Get all products with optional filtering"""
    try:
        # Build query
        query = {}
        if category:
            query["category"] = {"$regex": category, "$options": "i"}
        if featured is not None:
            query["featured"] = featured
        if search:
            query["$or"] = [
                {"name": {"$regex": search, "$options": "i"}},
                {"description": {"$regex": search, "$options": "i"}},
                {"tags": {"$in": [search]}}
            ]
        
        # Execute query with pagination
        cursor = db.products.find(query).skip(skip).limit(limit)
        products = await cursor.to_list(length=limit)
        
        return [Product(**product) for product in products]
    except Exception as e:
        logger.error(f"Error fetching products: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/{product_id}", response_model=Product)
async def get_product(product_id: str):
    """Get a single product by ID"""
    try:
        product = await db.products.find_one({"id": product_id})
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return Product(**product)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching product {product_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/", response_model=Product)
async def create_product(product: ProductCreate):
    """Create a new product"""
    try:
        product_dict = product.dict()
        new_product = Product(**product_dict)
        
        await db.products.insert_one(new_product.dict())
        return new_product
    except Exception as e:
        logger.error(f"Error creating product: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.put("/{product_id}", response_model=Product)
async def update_product(product_id: str, product_update: ProductUpdate):
    """Update a product"""
    try:
        # Check if product exists
        existing_product = await db.products.find_one({"id": product_id})
        if not existing_product:
            raise HTTPException(status_code=404, detail="Product not found")
        
        # Update product
        update_dict = {k: v for k, v in product_update.dict().items() if v is not None}
        if update_dict:
            await db.products.update_one(
                {"id": product_id},
                {"$set": update_dict}
            )
        
        # Return updated product
        updated_product = await db.products.find_one({"id": product_id})
        return Product(**updated_product)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating product {product_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.delete("/{product_id}")
async def delete_product(product_id: str):
    """Delete a product"""
    try:
        result = await db.products.delete_one({"id": product_id})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Product not found")
        return {"message": "Product deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting product {product_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")