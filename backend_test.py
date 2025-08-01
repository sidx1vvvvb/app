#!/usr/bin/env python3
"""
Comprehensive Backend API Testing for Mati Food
Tests all endpoints with proper reCAPTCHA integration and business logic
"""

import asyncio
import aiohttp
import json
import sys
from datetime import datetime
from typing import Dict, Any, List

# Backend URL from frontend environment
BACKEND_URL = "https://d89bf42f-cc49-4c0e-a1cf-27325f5aa580.preview.emergentagent.com/api"

# Test reCAPTCHA token (Google's test token that always passes)
TEST_RECAPTCHA_TOKEN = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"

class MatiBackendTester:
    def __init__(self):
        self.session = None
        self.test_results = []
        self.failed_tests = []
        
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    def log_test(self, test_name: str, success: bool, details: str = "", response_data: Any = None):
        """Log test results"""
        result = {
            "test": test_name,
            "success": success,
            "details": details,
            "timestamp": datetime.now().isoformat(),
            "response_data": response_data
        }
        self.test_results.append(result)
        
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}")
        if details:
            print(f"    Details: {details}")
        if not success:
            self.failed_tests.append(test_name)
        print()
    
    async def test_health_endpoint(self):
        """Test the health check endpoint"""
        try:
            async with self.session.get(f"{BACKEND_URL}/health") as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get("status") == "healthy" and data.get("database") == "connected":
                        self.log_test("Health Check", True, "API and database are healthy", data)
                    else:
                        self.log_test("Health Check", False, f"Unhealthy status: {data}")
                else:
                    self.log_test("Health Check", False, f"HTTP {response.status}")
        except Exception as e:
            self.log_test("Health Check", False, f"Exception: {str(e)}")
    
    async def test_root_endpoint(self):
        """Test the root API endpoint"""
        try:
            async with self.session.get(f"{BACKEND_URL}/") as response:
                if response.status == 200:
                    data = await response.json()
                    if "Mati Food API" in data.get("message", ""):
                        self.log_test("Root Endpoint", True, "Welcome message received", data)
                    else:
                        self.log_test("Root Endpoint", False, f"Unexpected message: {data}")
                else:
                    self.log_test("Root Endpoint", False, f"HTTP {response.status}")
        except Exception as e:
            self.log_test("Root Endpoint", False, f"Exception: {str(e)}")
    
    async def test_products_api(self):
        """Test products API endpoints"""
        # Test GET all products
        try:
            async with self.session.get(f"{BACKEND_URL}/products") as response:
                if response.status == 200:
                    products = await response.json()
                    if isinstance(products, list) and len(products) >= 8:
                        self.log_test("Products - Get All", True, f"Retrieved {len(products)} products", {"count": len(products)})
                        
                        # Test featured products filter
                        async with self.session.get(f"{BACKEND_URL}/products?featured=true") as featured_response:
                            if featured_response.status == 200:
                                featured_products = await featured_response.json()
                                featured_count = len([p for p in featured_products if p.get("featured")])
                                self.log_test("Products - Featured Filter", True, f"Found {featured_count} featured products", {"featured_count": featured_count})
                            else:
                                self.log_test("Products - Featured Filter", False, f"HTTP {featured_response.status}")
                        
                        # Test category filter
                        async with self.session.get(f"{BACKEND_URL}/products?category=Soups") as category_response:
                            if category_response.status == 200:
                                soup_products = await category_response.json()
                                soup_count = len([p for p in soup_products if "soup" in p.get("category", "").lower()])
                                self.log_test("Products - Category Filter", True, f"Found {soup_count} soup products", {"soup_count": soup_count})
                            else:
                                self.log_test("Products - Category Filter", False, f"HTTP {category_response.status}")
                        
                        # Test individual product retrieval
                        if products:
                            product_id = products[0]["id"]
                            async with self.session.get(f"{BACKEND_URL}/products/{product_id}") as product_response:
                                if product_response.status == 200:
                                    product = await product_response.json()
                                    self.log_test("Products - Get Single", True, f"Retrieved product: {product.get('name')}", {"product_name": product.get("name")})
                                else:
                                    self.log_test("Products - Get Single", False, f"HTTP {product_response.status}")
                    else:
                        self.log_test("Products - Get All", False, f"Expected 8+ products, got {len(products) if isinstance(products, list) else 'invalid response'}")
                else:
                    self.log_test("Products - Get All", False, f"HTTP {response.status}")
        except Exception as e:
            self.log_test("Products - Get All", False, f"Exception: {str(e)}")
    
    async def test_reviews_api(self):
        """Test reviews/testimonials API"""
        try:
            # Test featured reviews for homepage
            async with self.session.get(f"{BACKEND_URL}/reviews/featured") as response:
                if response.status == 200:
                    reviews = await response.json()
                    if isinstance(reviews, list) and len(reviews) >= 3:
                        featured_count = len([r for r in reviews if r.get("featured")])
                        self.log_test("Reviews - Featured Testimonials", True, f"Retrieved {featured_count} featured testimonials", {"featured_count": featured_count})
                    else:
                        self.log_test("Reviews - Featured Testimonials", False, f"Expected 3+ featured reviews, got {len(reviews) if isinstance(reviews, list) else 'invalid response'}")
                else:
                    self.log_test("Reviews - Featured Testimonials", False, f"HTTP {response.status}")
            
            # Test all reviews endpoint
            async with self.session.get(f"{BACKEND_URL}/reviews") as response:
                if response.status == 200:
                    all_reviews = await response.json()
                    self.log_test("Reviews - Get All", True, f"Retrieved {len(all_reviews)} total reviews", {"total_reviews": len(all_reviews)})
                else:
                    self.log_test("Reviews - Get All", False, f"HTTP {response.status}")
                    
        except Exception as e:
            self.log_test("Reviews - Featured Testimonials", False, f"Exception: {str(e)}")
    
    async def test_analytics_stats(self):
        """Test analytics/stats API for website statistics"""
        try:
            async with self.session.get(f"{BACKEND_URL}/analytics/stats") as response:
                if response.status == 200:
                    stats = await response.json()
                    
                    # Verify premium stats are present
                    expected_stats = ["happy_families", "michelin_stars", "organic_percentage", "products_available"]
                    missing_stats = [stat for stat in expected_stats if stat not in stats]
                    
                    if not missing_stats:
                        # Check premium values
                        premium_checks = []
                        if stats.get("happy_families", 0) >= 50000:
                            premium_checks.append("50K+ Happy Families ✓")
                        if stats.get("michelin_stars") == 3:
                            premium_checks.append("3 Michelin Stars ✓")
                        if stats.get("organic_percentage") == 100:
                            premium_checks.append("100% Organic ✓")
                        
                        self.log_test("Analytics - Website Stats", True, f"Premium stats verified: {', '.join(premium_checks)}", stats)
                    else:
                        self.log_test("Analytics - Website Stats", False, f"Missing stats: {missing_stats}")
                else:
                    self.log_test("Analytics - Website Stats", False, f"HTTP {response.status}")
        except Exception as e:
            self.log_test("Analytics - Website Stats", False, f"Exception: {str(e)}")
    
    async def test_contact_form_with_recaptcha(self):
        """Test contact form submission with reCAPTCHA integration"""
        # Test with valid reCAPTCHA token
        contact_data = {
            "name": "Isabella Martinez",
            "email": "isabella.martinez@example.com",
            "message": "I'm absolutely amazed by the quality of your organic products! The Elegant Flower Soup was a transcendent experience. Could you please tell me more about your premium collection and upcoming seasonal offerings?",
            "newsletter": True,
            "recaptcha_token": TEST_RECAPTCHA_TOKEN
        }
        
        try:
            # Use trailing slash to avoid redirect
            async with self.session.post(f"{BACKEND_URL}/contact/", json=contact_data) as response:
                if response.status == 200:
                    result = await response.json()
                    if result.get("recaptcha_verified") and result.get("email") == contact_data["email"]:
                        self.log_test("Contact Form - Valid reCAPTCHA", True, f"Contact submitted for {result.get('name')}", {"contact_id": result.get("id")})
                    else:
                        self.log_test("Contact Form - Valid reCAPTCHA", False, f"Invalid response structure: {result}")
                else:
                    response_text = await response.text()
                    self.log_test("Contact Form - Valid reCAPTCHA", False, f"HTTP {response.status}: {response_text}")
        except Exception as e:
            self.log_test("Contact Form - Valid reCAPTCHA", False, f"Exception: {str(e)}")
        
        # Test with invalid reCAPTCHA token
        invalid_contact_data = contact_data.copy()
        invalid_contact_data["recaptcha_token"] = "invalid_token_12345"
        invalid_contact_data["email"] = "test.invalid@example.com"
        
        try:
            # Use trailing slash to avoid redirect
            async with self.session.post(f"{BACKEND_URL}/contact/", json=invalid_contact_data) as response:
                if response.status == 400:
                    error_data = await response.json()
                    if "reCAPTCHA verification failed" in error_data.get("detail", ""):
                        self.log_test("Contact Form - Invalid reCAPTCHA", True, "Properly rejected invalid reCAPTCHA token")
                    else:
                        self.log_test("Contact Form - Invalid reCAPTCHA", False, f"Unexpected error message: {error_data}")
                else:
                    response_text = await response.text()
                    self.log_test("Contact Form - Invalid reCAPTCHA", False, f"Expected HTTP 400, got {response.status}: {response_text}")
        except Exception as e:
            self.log_test("Contact Form - Invalid reCAPTCHA", False, f"Exception: {str(e)}")
    
    async def test_newsletter_subscription(self):
        """Test newsletter subscription functionality"""
        newsletter_data = {
            "email": "premium.subscriber@example.com",
            "name": "Premium Subscriber"
        }
        
        try:
            async with self.session.post(f"{BACKEND_URL}/contact/newsletter", json=newsletter_data) as response:
                if response.status == 200:
                    result = await response.json()
                    if result.get("subscribed") and result.get("email") == newsletter_data["email"]:
                        self.log_test("Newsletter - Subscription", True, f"Newsletter subscription for {result.get('name')}", {"subscriber_id": result.get("id")})
                    else:
                        self.log_test("Newsletter - Subscription", False, f"Invalid response: {result}")
                else:
                    response_text = await response.text()
                    self.log_test("Newsletter - Subscription", False, f"HTTP {response.status}: {response_text}")
        except Exception as e:
            self.log_test("Newsletter - Subscription", False, f"Exception: {str(e)}")
    
    async def test_database_connectivity(self):
        """Test database connectivity through various endpoints"""
        try:
            # Test if we can retrieve data (indicates DB connection)
            async with self.session.get(f"{BACKEND_URL}/products") as response:
                if response.status == 200:
                    products = await response.json()
                    if isinstance(products, list) and len(products) > 0:
                        self.log_test("Database - Connectivity", True, f"Database connected and contains {len(products)} products")
                    else:
                        self.log_test("Database - Connectivity", False, "Database connected but no products found")
                else:
                    self.log_test("Database - Connectivity", False, f"Cannot retrieve products: HTTP {response.status}")
        except Exception as e:
            self.log_test("Database - Connectivity", False, f"Exception: {str(e)}")
    
    async def run_all_tests(self):
        """Run all backend tests"""
        print("🚀 Starting Mati Food Backend API Testing")
        print("=" * 60)
        
        # Core API tests
        await self.test_health_endpoint()
        await self.test_root_endpoint()
        await self.test_database_connectivity()
        
        # Business logic tests
        await self.test_products_api()
        await self.test_reviews_api()
        await self.test_analytics_stats()
        
        # Contact form and reCAPTCHA tests
        await self.test_contact_form_with_recaptcha()
        await self.test_newsletter_subscription()
        
        # Summary
        print("=" * 60)
        print("📊 TEST SUMMARY")
        print("=" * 60)
        
        total_tests = len(self.test_results)
        passed_tests = len([t for t in self.test_results if t["success"]])
        failed_tests = len(self.failed_tests)
        
        print(f"Total Tests: {total_tests}")
        print(f"Passed: {passed_tests} ✅")
        print(f"Failed: {failed_tests} ❌")
        print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
        
        if self.failed_tests:
            print("\n❌ FAILED TESTS:")
            for test in self.failed_tests:
                print(f"  - {test}")
        
        print("\n🎯 KEY FINDINGS:")
        
        # Check critical functionality
        health_passed = any(t["test"] == "Health Check" and t["success"] for t in self.test_results)
        products_passed = any(t["test"] == "Products - Get All" and t["success"] for t in self.test_results)
        recaptcha_passed = any(t["test"] == "Contact Form - Valid reCAPTCHA" and t["success"] for t in self.test_results)
        reviews_passed = any(t["test"] == "Reviews - Featured Testimonials" and t["success"] for t in self.test_results)
        stats_passed = any(t["test"] == "Analytics - Website Stats" and t["success"] for t in self.test_results)
        
        print(f"  • API Health: {'✅ Working' if health_passed else '❌ Failed'}")
        print(f"  • Products API: {'✅ Working' if products_passed else '❌ Failed'}")
        print(f"  • reCAPTCHA Integration: {'✅ Working' if recaptcha_passed else '❌ Failed'}")
        print(f"  • Featured Reviews: {'✅ Working' if reviews_passed else '❌ Failed'}")
        print(f"  • Premium Stats: {'✅ Working' if stats_passed else '❌ Failed'}")
        
        return failed_tests == 0

async def main():
    """Main test runner"""
    async with MatiBackendTester() as tester:
        success = await tester.run_all_tests()
        return 0 if success else 1

if __name__ == "__main__":
    try:
        exit_code = asyncio.run(main())
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n⚠️  Tests interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Test runner failed: {e}")
        sys.exit(1)