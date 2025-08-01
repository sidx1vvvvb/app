from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime
import uuid

class Contact(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: EmailStr
    message: str
    newsletter: bool = False
    status: str = "new"  # 'new', 'read', 'replied'
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class ContactCreate(BaseModel):
    name: str
    email: EmailStr
    message: str
    newsletter: bool = False

class ContactUpdate(BaseModel):
    status: Optional[str] = None
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class Newsletter(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    name: Optional[str] = None
    subscribed: bool = True
    subscribed_at: datetime = Field(default_factory=datetime.utcnow)
    unsubscribed_at: Optional[datetime] = None

class NewsletterCreate(BaseModel):
    email: EmailStr
    name: Optional[str] = None