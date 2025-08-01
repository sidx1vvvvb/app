from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid

class Product(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    category: str
    price: float
    original_price: Optional[float] = None
    image: str
    images: Optional[List[str]] = []
    description: str
    long_description: Optional[str] = None
    ingredients: Optional[List[str]] = []
    nutrition_facts: Optional[dict] = {}
    in_stock: bool = True
    stock_quantity: int = 100
    rating: float = 5.0
    review_count: int = 0
    featured: bool = False
    organic: bool = True
    tags: Optional[List[str]] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class ProductCreate(BaseModel):
    name: str
    category: str
    price: float
    original_price: Optional[float] = None
    image: str
    images: Optional[List[str]] = []
    description: str
    long_description: Optional[str] = None
    ingredients: Optional[List[str]] = []
    nutrition_facts: Optional[dict] = {}
    stock_quantity: int = 100
    featured: bool = False
    tags: Optional[List[str]] = []

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = None
    original_price: Optional[float] = None
    image: Optional[str] = None
    images: Optional[List[str]] = None
    description: Optional[str] = None
    long_description: Optional[str] = None
    ingredients: Optional[List[str]] = None
    nutrition_facts: Optional[dict] = None
    in_stock: Optional[bool] = None
    stock_quantity: Optional[int] = None
    featured: Optional[bool] = None
    tags: Optional[List[str]] = None
    updated_at: datetime = Field(default_factory=datetime.utcnow)