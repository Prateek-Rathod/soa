# Online Shopping System

A microservices-based online shopping system built using Service-Oriented Architecture (SOA).

## Services

1. **Product Service** (Port: 5000)
   - Python/Flask
   - Manages product catalog
   - Endpoints:
     - GET /products
     - POST /products

2. **Auth Service** (Port: 5001)
   - Node.js/Express
   - Handles user authentication
   - Endpoints:
     - POST /register

3. **Cart Service** (Port: 5002)
   - Node.js/Express
   - Manages shopping cart
   - Endpoints:
     - POST /cart/add
     - GET /cart/:userId

4. **Order Service** (Port: 5003)
   - Java/Spring Boot
   - Handles order management
   - Endpoints:
     - POST /orders
     - GET /orders

5. **Payment Service** (Port: 5004)
   - Python/Flask
   - Processes payments
   - Endpoints:
     - POST /pay

## Prerequisites

- Docker
- Docker Compose

## Running the Application

1. Clone the repository
2. Navigate to the project directory
3. Run the following command:
   ```bash
   docker-compose up --build
   ```

This will start all services and their dependencies (MongoDB and Redis).

## Service URLs

- Product Service: http://localhost:5000
- Auth Service: http://localhost:5001
- Cart Service: http://localhost:5002
- Order Service: http://localhost:5003
- Payment Service: http://localhost:5004

## Testing the Services

You can use tools like Postman or curl to test the endpoints. Here are some example requests:

1. Create a product:
```bash
curl -X POST http://localhost:5000/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Product", "price": 99.99, "description": "Test Description"}'
```

2. Register a user:
```bash
curl -X POST http://localhost:5001/register \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "password123", "email": "test@example.com"}'
```

3. Add item to cart:
```bash
curl -X POST http://localhost:5002/cart/add \
  -H "Content-Type: application/json" \
  -d '{"userId": 1, "productId": 1, "quantity": 1}'
```

4. Create an order:
```bash
curl -X POST http://localhost:5003/orders \
  -H "Content-Type: application/json" \
  -d '{"userId": 1, "totalAmount": 99.99}'
```

5. Process payment:
```bash
curl -X POST http://localhost:5004/pay \
  -H "Content-Type: application/json" \
  -d '{"amount": 99.99}'
```

## Architecture

The system uses a microservices architecture where each service is independently deployable and scalable. Services communicate over HTTP and are containerized using Docker. The system includes:

- MongoDB for user data storage
- Redis for cart data storage
- H2 Database for order storage (embedded)

## Notes

- This is a basic implementation for demonstration purposes
- In a production environment, you would want to add:
  - Authentication and authorization
  - API gateways
  - Service discovery
  - Load balancing
  - Proper error handling
  - Logging and monitoring
  - SSL/TLS encryption 