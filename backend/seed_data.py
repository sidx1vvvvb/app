from datetime import datetime
from .database import db
import logging

logger = logging.getLogger(__name__)

# Premium seed data for the award-winning Mati Food website
SEED_PRODUCTS = [
    {
        "id": "1",
        "name": "Organic Vegetable Soup Mix",
        "category": "Soups",
        "price": 12.99,
        "original_price": 19.99,
        "image": "https://images.unsplash.com/photo-1679949479680-c65ef800b48b?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3MjQyMTd8MHwxfHNlYXJjaHwxfHxvcmdhbmljJTIwc291cCUyMGJvd2xzfGVufDB8fHx8MTc1NDA2MjQ3NHww&ixlib=rb-4.1.0&q=85",
        "description": "A nutritious blend of organic vegetables perfect for creating hearty, wholesome soups. Made with premium ingredients sourced from certified organic farms.",
        "long_description": "Our signature Organic Vegetable Soup Mix represents three generations of culinary mastery. Each ingredient is hand-selected at the peak of ripeness from our partner organic farms nestled in pristine valleys. This extraordinary blend combines heirloom vegetables with ancient grains, creating a symphony of flavors that nourishes both body and soul.",
        "ingredients": ["Organic Carrots", "Organic Celery", "Organic Onions", "Organic Herbs", "Sea Salt"],
        "nutrition_facts": {"calories": 45, "protein": "2g", "fiber": "3g", "sodium": "120mg"},
        "rating": 4.9,
        "review_count": 347,
        "featured": True,
        "organic": True,
        "tags": ["vegetarian", "gluten-free", "organic", "premium"],
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    },
    {
        "id": "2",
        "name": "Natural Green Smoothie Bowl",
        "category": "Smoothies",
        "price": 8.99,
        "original_price": 12.99,
        "image": "https://images.unsplash.com/photo-1590794056675-8354831935b2?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3MjQyMTd8MHwxfHNlYXJjaHwyfHxvcmdhbmljJTIwc291cCUyMGJvd2xzfGVufDB8fHx8MTc1NDA2MjQ3NHww&ixlib=rb-4.1.0&q=85",
        "description": "Fresh, nutrient-packed green smoothie blend featuring organic spinach, kale, and superfoods. Perfect for a healthy start to your day.",
        "long_description": "Awaken your senses with our Natural Green Smoothie Bowl - a vibrant celebration of nature's finest superfoods. Crafted with love from organic spinach, baby kale, and exotic superfruits, this emerald elixir is more than nutrition; it's pure liquid vitality that energizes your soul.",
        "ingredients": ["Organic Spinach", "Organic Kale", "Organic Spirulina", "Coconut Water", "Natural Flavors"],
        "nutrition_facts": {"calories": 65, "protein": "4g", "fiber": "5g", "vitamin_c": "80mg"},
        "rating": 4.8,
        "review_count": 289,
        "featured": True,
        "organic": True,
        "tags": ["vegan", "superfood", "organic", "detox"],
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    },
    {
        "id": "3",
        "name": "Premium Tomato Basil Soup",
        "category": "Soups",
        "price": 10.99,
        "original_price": 14.99,
        "image": "https://images.pexels.com/photos/262947/pexels-photo-262947.jpeg",
        "description": "Rich and creamy tomato soup made with vine-ripened organic tomatoes and fresh basil. A classic comfort food with a natural twist.",
        "long_description": "Experience the essence of summer in every spoonful of our Premium Tomato Basil Soup. Made from heirloom tomatoes that have basked in Mediterranean sunshine and fresh basil grown in our sacred gardens, this liquid poetry captures the soul of traditional Italian cuisine with a luxurious organic touch.",
        "ingredients": ["Organic Vine Tomatoes", "Fresh Basil", "Organic Cream", "Sea Salt", "Organic Herbs"],
        "nutrition_facts": {"calories": 78, "protein": "3g", "fiber": "2g", "vitamin_a": "25%"},
        "rating": 4.9,
        "review_count": 456,
        "featured": True,
        "organic": True,
        "tags": ["vegetarian", "comfort-food", "organic", "premium"],
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    },
    {
        "id": "4",
        "name": "Golden Turmeric Broth",
        "category": "Broths",
        "price": 14.99,
        "original_price": 19.99,
        "image": "https://images.pexels.com/photos/5662121/pexels-photo-5662121.jpeg",
        "description": "Anti-inflammatory golden broth infused with organic turmeric, ginger, and healing spices. Perfect for wellness and recovery.",
        "long_description": "Discover the ancient wisdom of our Golden Turmeric Broth - a sacred elixir crafted from centuries-old Ayurvedic traditions. Each sip delivers the healing power of organic turmeric, wild ginger, and mystical spices that have been cherished by wellness masters for generations.",
        "ingredients": ["Organic Turmeric", "Wild Ginger", "Black Pepper", "Coconut Milk", "Healing Spices"],
        "nutrition_facts": {"calories": 52, "protein": "2g", "curcumin": "95mg", "antioxidants": "High"},
        "rating": 4.9,
        "review_count": 234,
        "featured": False,
        "organic": True,
        "tags": ["wellness", "anti-inflammatory", "organic", "healing"],
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    },
    {
        "id": "5",
        "name": "Artisan Fruit Preserves",
        "category": "Preserves",
        "price": 15.99,
        "original_price": 21.99,
        "image": "https://images.pexels.com/photos/48817/jam-preparations-jars-fruit-48817.jpeg",
        "description": "Handcrafted fruit preserves made from organic seasonal fruits. No artificial preservatives, just pure natural sweetness.",
        "long_description": "Our Artisan Fruit Preserves are love letters written in the language of taste. Master craftsmen carefully select only the most perfect organic fruits at the moment of peak ripeness, transforming them into liquid gold that captures the essence of each season in a jar.",
        "ingredients": ["Organic Seasonal Fruits", "Organic Cane Sugar", "Lemon Juice", "Natural Pectin"],
        "nutrition_facts": {"calories": 35, "sugar": "8g", "fiber": "1g", "vitamin_c": "12mg"},
        "rating": 4.8,
        "review_count": 178,
        "featured": False,
        "organic": True,
        "tags": ["handcrafted", "seasonal", "organic", "artisan"],
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    },
    {
        "id": "6",
        "name": "Mixed Nuts & Seeds Bowl",
        "category": "Snacks",
        "price": 11.99,
        "original_price": 15.99,
        "image": "https://images.pexels.com/photos/1306548/pexels-photo-1306548.jpeg",
        "description": "Premium mix of organic nuts and seeds, perfect for snacking or adding to your favorite dishes. Rich in healthy fats and protein.",
        "long_description": "Indulge in nature's perfect snack with our Mixed Nuts & Seeds Bowl. Each nut and seed has been carefully sourced from sustainable organic farms and roasted to perfection by our master artisans, creating a symphony of textures and flavors that nourish both body and soul.",
        "ingredients": ["Organic Almonds", "Organic Walnuts", "Organic Pumpkin Seeds", "Organic Sunflower Seeds", "Sea Salt"],
        "nutrition_facts": {"calories": 165, "protein": "7g", "healthy_fats": "14g", "fiber": "3g"},
        "rating": 4.7,
        "review_count": 312,
        "featured": False,
        "organic": True,
        "tags": ["protein", "healthy-fats", "organic", "snack"],
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    },
    {
        "id": "7",
        "name": "Elegant Flower Soup",
        "category": "Gourmet",
        "price": 18.99,
        "original_price": 24.99,
        "image": "https://images.unsplash.com/photo-1594306627270-88a533d13bf8?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3MjQyMTd8MHwxfHNlYXJjaHw0fHxvcmdhbmljJTIwc291cCUyMGJvd2xzfGVufDB8fHx8MTc1NDA2MjQ3NHww&ixlib=rb-4.1.0&q=85",
        "description": "Gourmet soup blend enhanced with edible flowers and premium ingredients. A sophisticated dining experience with natural elegance.",
        "long_description": "Experience culinary artistry at its finest with our Elegant Flower Soup. This masterpiece combines the delicate beauty of organic edible flowers with the richest flavors nature can offer, creating an ethereal dining experience that transcends ordinary cuisine and becomes liquid poetry.",
        "ingredients": ["Organic Edible Flowers", "Vegetable Broth", "Organic Cream", "Herbs de Provence", "Truffle Oil"],
        "nutrition_facts": {"calories": 89, "protein": "4g", "fiber": "2g", "antioxidants": "Very High"},
        "rating": 5.0,
        "review_count": 67,
        "featured": True,
        "organic": True,
        "tags": ["gourmet", "luxury", "organic", "edible-flowers"],
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    },
    {
        "id": "8",
        "name": "Traditional Herbal Broth",
        "category": "Broths",
        "price": 13.99,
        "original_price": 17.99,
        "image": "https://images.unsplash.com/photo-1704642155498-70b60672f1f3?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3MjQyMTd8MHwxfHNlYXJjaHwzfHxvcmdhbmljJTIwc291cCUyMGJvd2xzfGVufDB8fHx8MTc1NDA2MjQ3NHww&ixlib=rb-4.1.0&q=85",
        "description": "Time-honored herbal broth recipe using traditional healing herbs and organic ingredients. Perfect for nourishment and wellness.",
        "long_description": "Our Traditional Herbal Broth carries the wisdom of ancient healers and the love of countless generations. Crafted from sacred herbs and organic ingredients following time-honored recipes, this healing elixir offers comfort, nourishment, and the profound connection to nature's healing power.",
        "ingredients": ["Traditional Herbs", "Organic Vegetables", "Healing Spices", "Pure Water", "Sea Salt"],
        "nutrition_facts": {"calories": 38, "protein": "2g", "minerals": "High", "herbs": "Traditional Blend"},
        "rating": 4.8,
        "review_count": 189,
        "featured": False,
        "organic": True,
        "tags": ["traditional", "healing", "organic", "wellness"],
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
]

SEED_REVIEWS = [
    {
        "id": "r1",
        "product_id": None,  # General testimonial
        "customer_name": "Sarah Johnson",
        "customer_email": "sarah.j@email.com",
        "rating": 5,
        "comment": "The quality of Mati Food products is exceptional. I can taste the difference in every bite - truly natural and organic! My family has been transformed by these incredible flavors.",
        "verified": True,
        "featured": True,
        "avatar": "https://images.unsplash.com/photo-1494790108755-2616b612b762?w=150&h=150&fit=crop&crop=face",
        "created_at": datetime.utcnow()
    },
    {
        "id": "r2",
        "product_id": None,
        "customer_name": "Michael Chen",
        "customer_email": "m.chen@email.com",
        "rating": 5,
        "comment": "As someone who cares about healthy eating, Mati Food has become my go-to source for premium organic products. The artistry in every bowl is simply breathtaking.",
        "verified": True,
        "featured": True,
        "avatar": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=150&h=150&fit=crop&crop=face",
        "created_at": datetime.utcnow()
    },
    {
        "id": "r3",
        "product_id": None,
        "customer_name": "Emily Rodriguez",
        "customer_email": "emily.r@email.com",
        "rating": 5,
        "comment": "The soups are absolutely delicious and you can really taste the quality of the organic ingredients. This isn't just food - it's liquid poetry that nourishes my soul. Highly recommended!",
        "verified": True,
        "featured": True,
        "avatar": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=150&h=150&fit=crop&crop=face",
        "created_at": datetime.utcnow()
    }
]

async def seed_database():
    """Seed the database with initial premium data"""
    try:
        # Clear existing data
        await db.products.delete_many({})
        await db.reviews.delete_many({})
        
        # Insert products
        if SEED_PRODUCTS:
            await db.products.insert_many(SEED_PRODUCTS)
            logger.info(f"Seeded {len(SEED_PRODUCTS)} products")
        
        # Insert reviews
        if SEED_REVIEWS:
            await db.reviews.insert_many(SEED_REVIEWS)
            logger.info(f"Seeded {len(SEED_REVIEWS)} reviews")
        
        logger.info("Database seeded successfully with premium Mati Food data")
        return True
    except Exception as e:
        logger.error(f"Error seeding database: {e}")
        return False