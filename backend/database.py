from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging

logger = logging.getLogger(__name__)

# MongoDB connection
mongo_url = os.environ.get('MONGO_URL', 'mongodb://localhost:27017/matifood')
db_name = os.environ.get('DB_NAME', 'matifood')

try:
    client = AsyncIOMotorClient(mongo_url)
    db = client[db_name]
    logger.info(f"Connected to MongoDB: {db_name}")
except Exception as e:
    logger.error(f"Failed to connect to MongoDB: {e}")
    raise

# Test connection
async def test_connection():
    try:
        await client.admin.command('ping')
        logger.info("MongoDB connection successful")
        return True
    except Exception as e:
        logger.error(f"MongoDB connection failed: {e}")
        return False