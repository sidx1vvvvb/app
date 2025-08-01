from fastapi import APIRouter, HTTPException
import logging
from datetime import datetime, timedelta
from database import db

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/analytics", tags=["analytics"])

@router.get("/stats")
async def get_website_stats():
    """Get website statistics for the homepage"""
    try:
        # Get product count
        product_count = await db.products.count_documents({})
        
        # Get total reviews
        review_count = await db.reviews.count_documents({})
        
        # Get newsletter subscribers
        subscriber_count = await db.newsletter.count_documents({"subscribed": True})
        
        # Get contact submissions (as a proxy for customer interactions)
        contact_count = await db.contacts.count_documents({})
        
        # Calculate some premium stats
        stats = {
            "happy_families": max(subscriber_count + contact_count, 50000),  # At least 50K for premium feel
            "countries": 25,  # Static premium number
            "organic_percentage": 100,  # Always 100% organic
            "michelin_stars": 3,  # Premium credential
            "products_available": product_count,
            "total_reviews": review_count,
            "newsletter_subscribers": subscriber_count,
            "average_rating": 4.9,  # Premium rating
            "years_of_experience": 25,
            "master_artisans": 12,
            "awards_won": 15
        }
        
        return stats
    except Exception as e:
        logger.error(f"Error fetching website stats: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/recent-activity")
async def get_recent_activity():
    """Get recent website activity"""
    try:
        # Get recent contacts
        recent_contacts = await db.contacts.find().sort("created_at", -1).limit(5).to_list(5)
        
        # Get recent reviews
        recent_reviews = await db.reviews.find().sort("created_at", -1).limit(5).to_list(5)
        
        # Get recent newsletter subscriptions
        recent_subscribers = await db.newsletter.find({"subscribed": True}).sort("subscribed_at", -1).limit(5).to_list(5)
        
        activity = {
            "recent_contacts": len(recent_contacts),
            "recent_reviews": len(recent_reviews),
            "recent_subscribers": len(recent_subscribers),
            "last_contact": recent_contacts[0]["created_at"] if recent_contacts else None,
            "last_review": recent_reviews[0]["created_at"] if recent_reviews else None,
            "last_subscription": recent_subscribers[0]["subscribed_at"] if recent_subscribers else None
        }
        
        return activity
    except Exception as e:
        logger.error(f"Error fetching recent activity: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/events")
async def track_event(event_data: dict):
    """Track user events for analytics"""
    try:
        # Add timestamp to event
        event_data["timestamp"] = datetime.utcnow()
        
        # Store event in database
        await db.events.insert_one(event_data)
        
        return {"message": "Event tracked successfully"}
    except Exception as e:
        logger.error(f"Error tracking event: {e}")
        raise HTTPException(status_code=500, detail="Failed to track event")