from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path

# Import route modules
from routes import products, contact, reviews, analytics
from database import test_connection
from seed_data import seed_database

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create the main app
app = FastAPI(title="Mati Food API", description="Premium Organic Food API", version="1.0.0")

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include route modules
api_router.include_router(products.router)
api_router.include_router(contact.router)
api_router.include_router(reviews.router)
api_router.include_router(analytics.router)

# Basic health check endpoint
@api_router.get("/")
async def root():
    return {"message": "Welcome to Mati Food API - Taste the Goodness of Nature", "version": "1.0.0"}

@api_router.get("/health")
async def health_check():
    """Health check endpoint"""
    db_status = await test_connection()
    return {
        "status": "healthy" if db_status else "unhealthy",
        "database": "connected" if db_status else "disconnected",
        "message": "Mati Food API is running"
    }

# Include the router in the main app
app.include_router(api_router)

@app.on_event("startup")
async def startup_event():
    """Initialize the application"""
    logger.info("Starting Mati Food API...")
    
    # Test database connection
    db_connected = await test_connection()
    if not db_connected:
        logger.error("Failed to connect to database")
        return
    
    # Seed database with initial data
    try:
        # Check if products exist
        from database import db
        product_count = await db.products.count_documents({})
        if product_count == 0:
            logger.info("No products found, seeding database...")
            await seed_database()
        else:
            logger.info(f"Database already contains {product_count} products")
    except Exception as e:
        logger.error(f"Error during startup: {e}")
    
    logger.info("Mati Food API started successfully!")

@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    logger.info("Shutting down Mati Food API...")
    # Any cleanup code here
