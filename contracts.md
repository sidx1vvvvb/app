# Mati Food - Full Stack Integration Contracts

## API Endpoints to Implement

### 1. Products API
- `GET /api/products` - Get all products with pagination and filtering
- `GET /api/products/:id` - Get single product details
- `POST /api/products` - Create new product (admin)
- `PUT /api/products/:id` - Update product (admin)
- `DELETE /api/products/:id` - Delete product (admin)

### 2. Contact API
- `POST /api/contact` - Submit contact form
- `GET /api/contact` - Get all contact submissions (admin)
- `POST /api/newsletter` - Subscribe to newsletter

### 3. Reviews/Testimonials API
- `GET /api/reviews` - Get featured reviews
- `POST /api/reviews` - Submit product review
- `GET /api/reviews/product/:productId` - Get reviews for specific product

### 4. Analytics API
- `GET /api/stats` - Get website statistics (visitors, orders, etc.)
- `POST /api/events` - Track user events

## Data Models

### Product Model
```javascript
{
  _id: ObjectId,
  name: String,
  category: String,
  price: Number,
  originalPrice: Number,
  image: String,
  images: [String], // Additional product images
  description: String,
  longDescription: String,
  ingredients: [String],
  nutritionFacts: Object,
  inStock: Boolean,
  stockQuantity: Number,
  rating: Number,
  reviewCount: Number,
  featured: Boolean,
  organic: Boolean,
  tags: [String],
  createdAt: Date,
  updatedAt: Date
}
```

### Contact Model
```javascript
{
  _id: ObjectId,
  name: String,
  email: String,
  message: String,
  newsletter: Boolean,
  status: String, // 'new', 'read', 'replied'
  createdAt: Date,
  updatedAt: Date
}
```

### Review Model
```javascript
{
  _id: ObjectId,
  productId: ObjectId,
  customerName: String,
  customerEmail: String,
  rating: Number,
  comment: String,
  verified: Boolean,
  featured: Boolean,
  createdAt: Date
}
```

### Newsletter Model
```javascript
{
  _id: ObjectId,
  email: String,
  name: String,
  subscribed: Boolean,
  subscribedAt: Date,
  unsubscribedAt: Date
}
```

## Currently Mocked Data (Frontend)

### In `/app/frontend/src/data/mockData.js`:
1. **mockProducts** - 8 premium organic products with images, prices, descriptions
2. **mockContactInfo** - Company contact details
3. **mockTestimonials** - Customer reviews and ratings

## Frontend-Backend Integration Plan

### Phase 1: Products Integration
- Replace `mockProducts` import with API call to `/api/products`
- Update ProductsSection.jsx to fetch from backend
- Add loading states and error handling
- Implement product filtering and pagination

### Phase 2: Contact Form Integration
- Update ContactSection.jsx to submit to `/api/contact`
- Add form validation and submission states
- Implement newsletter subscription to `/api/newsletter`
- Show success/error messages using toast system

### Phase 3: Dynamic Content
- Replace static testimonials with `/api/reviews`
- Update stats counters with real data from `/api/stats`
- Add dynamic content management

### Phase 4: Enhanced Features
- Product search functionality
- Product detail pages
- Shopping cart (if needed)
- Admin dashboard for content management

## Environment Variables Needed
```
MONGO_URL=mongodb://localhost:27017/matifood
DB_NAME=matifood
JWT_SECRET=your-secret-key
SMTP_HOST=smtp.gmail.com (for email notifications)
SMTP_PORT=587
SMTP_USER=your-email
SMTP_PASS=your-password
```

## Error Handling Strategy
- Consistent error response format
- Graceful fallbacks to cached/mock data
- User-friendly error messages
- Loading states for all async operations

## Performance Optimizations
- Image optimization and lazy loading
- API response caching
- Database indexing on frequently queried fields
- Pagination for large datasets

## Security Considerations
- Input validation and sanitization
- Rate limiting on contact form
- CORS configuration
- Data encryption for sensitive information