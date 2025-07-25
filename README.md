<<<<<<< HEAD
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
=======
# Online Shopping System using SOA

A modern e-commerce system built using Service-Oriented Architecture (SOA) principles and microservices.

## 🏗️ Architecture

The system consists of five microservices:

1. **Product Service** (Python/Flask)
   - Product catalog management
   - Port: 5000

2. **Auth Service** (Node.js/Express)
   - User authentication
   - Port: 5001

3. **Cart Service** (Node.js/Express)
   - Shopping cart management
   - Port: 5002

4. **Order Service** (Java/Spring Boot)
   - Order processing
   - Port: 5003

5. **Payment Service** (Python/Flask)
   - Payment processing
   - Port: 5004

## 🚀 Getting Started

### Prerequisites
- Docker
- Docker Compose

### Running the Application

1. Clone the repository:
```bash
git clone https://github.com/Prateek-Rathod/soa.git
cd soa
```

2. Start the services:
```bash
docker-compose up --build
```

3. Access the services:
- Product Service: http://localhost:5000/docs
- Auth Service: http://localhost:5001/docs
- Cart Service: http://localhost:5002/docs
- Order Service: http://localhost:5003
- Payment Service: http://localhost:5004/docs

## 📝 API Documentation

Each service provides Swagger/OpenAPI documentation at its `/docs` endpoint.

### Example API Calls

1. View Products:
```bash
curl http://localhost:5000/products
```

2. Register User:
>>>>>>> 5a5511c5bd534985ba6783977d260f7427f04bd1
```bash
curl -X POST http://localhost:5001/register \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "password123", "email": "test@example.com"}'
```

<<<<<<< HEAD
3. Add item to cart:
```bash
curl -X POST http://localhost:5002/cart/add \
  -H "Content-Type: application/json" \
  -d '{"userId": 1, "productId": 1, "quantity": 1}'
```

4. Create an order:
=======
3. Add to Cart:
```bash
curl -X POST http://localhost:5002/cart/add \
  -H "Content-Type: application/json" \
  -d '{"userId": 1, "productId": 1, "quantity": 2}'
```

4. Create Order:
>>>>>>> 5a5511c5bd534985ba6783977d260f7427f04bd1
```bash
curl -X POST http://localhost:5003/orders \
  -H "Content-Type: application/json" \
  -d '{"userId": 1, "totalAmount": 99.99}'
```

<<<<<<< HEAD
5. Process payment:
=======
5. Process Payment:
>>>>>>> 5a5511c5bd534985ba6783977d260f7427f04bd1
```bash
curl -X POST http://localhost:5004/pay \
  -H "Content-Type: application/json" \
  -d '{"amount": 99.99}'
```

<<<<<<< HEAD
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
=======
## 🛠️ Technology Stack

- **Languages & Frameworks**:
  - Python (Flask)
  - Node.js (Express)
  - Java (Spring Boot)

- **Databases**:
  - MongoDB (User data)
  - Redis (Cart data)
  - H2 (Order data)

- **Documentation**:
  - Swagger/OpenAPI

- **Containerization**:
  - Docker
  - Docker Compose

## 📊 Features

- Microservices Architecture
- Container-based Deployment
- API Documentation
- Independent Scaling
- Error Handling
- Cross-Origin Support

## 🔒 Security

- Password Hashing
- Input Validation
- Error Handling
- Secure Communication

## 🔄 Service Communication

All services communicate via RESTful APIs using JSON for data exchange.

## 📈 Future Enhancements

- API Gateway
- Service Discovery
- Load Balancing
- Advanced Monitoring
- Caching Layer

## 👥 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License. 
>>>>>>> 5a5511c5bd534985ba6783977d260f7427f04bd1
