from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime
import uuid

class Review(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    product_id: Optional[str] = None  # If None, it's a general testimonial
    customer_name: str
    customer_email: Optional[EmailStr] = None
    rating: int = Field(ge=1, le=5)
    comment: str
    verified: bool = False
    featured: bool = False
    avatar: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ReviewCreate(BaseModel):
    product_id: Optional[str] = None
    customer_name: str
    customer_email: Optional[EmailStr] = None
    rating: int = Field(ge=1, le=5)
    comment: str
    avatar: Optional[str] = None

class ReviewUpdate(BaseModel):
    verified: Optional[bool] = None
    featured: Optional[bool] = None