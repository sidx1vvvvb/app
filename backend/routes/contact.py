from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
import logging
from ..models.Contact import Contact, ContactCreate, ContactUpdate, Newsletter, NewsletterCreate
from ..database import db

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/contact", tags=["contact"])

@router.post("/", response_model=Contact)
async def submit_contact_form(contact: ContactCreate):
    """Submit a contact form"""
    try:
        contact_dict = contact.dict()
        new_contact = Contact(**contact_dict)
        
        # Save contact to database
        await db.contacts.insert_one(new_contact.dict())
        
        # If user wants newsletter, subscribe them
        if contact.newsletter:
            try:
                newsletter_data = NewsletterCreate(
                    email=contact.email,
                    name=contact.name
                )
                await subscribe_to_newsletter(newsletter_data)
            except Exception as e:
                logger.warning(f"Failed to subscribe to newsletter: {e}")
        
        logger.info(f"New contact submission from {contact.email}")
        return new_contact
    except Exception as e:
        logger.error(f"Error submitting contact form: {e}")
        raise HTTPException(status_code=500, detail="Failed to submit contact form")

@router.get("/", response_model=List[Contact])
async def get_contacts(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    status: Optional[str] = None
):
    """Get all contact submissions (admin endpoint)"""
    try:
        query = {}
        if status:
            query["status"] = status
        
        cursor = db.contacts.find(query).sort("created_at", -1).skip(skip).limit(limit)
        contacts = await cursor.to_list(length=limit)
        
        return [Contact(**contact) for contact in contacts]
    except Exception as e:
        logger.error(f"Error fetching contacts: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.put("/{contact_id}", response_model=Contact)
async def update_contact_status(contact_id: str, contact_update: ContactUpdate):
    """Update contact status (admin endpoint)"""
    try:
        # Check if contact exists
        existing_contact = await db.contacts.find_one({"id": contact_id})
        if not existing_contact:
            raise HTTPException(status_code=404, detail="Contact not found")
        
        # Update contact
        update_dict = {k: v for k, v in contact_update.dict().items() if v is not None}
        if update_dict:
            await db.contacts.update_one(
                {"id": contact_id},
                {"$set": update_dict}
            )
        
        # Return updated contact
        updated_contact = await db.contacts.find_one({"id": contact_id})
        return Contact(**updated_contact)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating contact {contact_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/newsletter", response_model=Newsletter)
async def subscribe_to_newsletter(newsletter: NewsletterCreate):
    """Subscribe to newsletter"""
    try:
        # Check if email already exists
        existing_subscription = await db.newsletter.find_one({"email": newsletter.email})
        if existing_subscription:
            # If unsubscribed, resubscribe
            if not existing_subscription.get("subscribed", True):
                await db.newsletter.update_one(
                    {"email": newsletter.email},
                    {"$set": {"subscribed": True, "unsubscribed_at": None}}
                )
                updated_sub = await db.newsletter.find_one({"email": newsletter.email})
                return Newsletter(**updated_sub)
            else:
                # Already subscribed
                return Newsletter(**existing_subscription)
        
        # New subscription
        newsletter_dict = newsletter.dict()
        new_subscription = Newsletter(**newsletter_dict)
        
        await db.newsletter.insert_one(new_subscription.dict())
        logger.info(f"New newsletter subscription: {newsletter.email}")
        return new_subscription
    except Exception as e:
        logger.error(f"Error subscribing to newsletter: {e}")
        raise HTTPException(status_code=500, detail="Failed to subscribe to newsletter")

@router.delete("/newsletter/{email}")
async def unsubscribe_from_newsletter(email: str):
    """Unsubscribe from newsletter"""
    try:
        from datetime import datetime
        
        result = await db.newsletter.update_one(
            {"email": email},
            {"$set": {"subscribed": False, "unsubscribed_at": datetime.utcnow()}}
        )
        
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Email not found in newsletter")
        
        return {"message": "Successfully unsubscribed from newsletter"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error unsubscribing from newsletter: {e}")
        raise HTTPException(status_code=500, detail="Failed to unsubscribe from newsletter")