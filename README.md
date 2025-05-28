# 🛒 FastAPI E-commerce API

A modern, high-performance e-commerce REST API built with FastAPI, featuring user authentication, product management, shopping cart functionality, and order processing.

---

## 🚀 Features

### 👤 User Management
- User registration and authentication  
- JWT-based authorization  
- Profile management  
- Email validation  

### 📦 Product Management
- CRUD operations for products  
- Product categorization  
- Image upload support  
- Search and filtering  

### 🛍️ Shopping Cart
- Add/remove items from cart  
- Update quantities  
- Persistent cart storage  

### 📦 Order Management
- Order creation and tracking  
- Order history  
- Status updates  

### 🌟 Review System
- Product reviews and ratings  
- User feedback management  

---

## 🛠️ Tech Stack

- **Framework:** FastAPI  
- **Database:** PostgreSQL / SQLite  
- **Authentication:** JWT tokens  
- **Validation:** Pydantic v2  
- **ORM:** SQLAlchemy  
- **Password Hashing:** Passlib with bcrypt  
- **API Documentation:** Swagger UI (auto-generated)  

---

## 📋 Prerequisites

- Python 3.8+  
- pip or pipenv  
- PostgreSQL (optional) or SQLite (for development)  

---

## 🔧 Installation

### 1. Clone the repository
```bash
git clone https://github.com/Ktrimalrao/ecommerce-backend-fastapi
cd ecommerce-backend-fastapi

```
### 2. Create and activate a virtual environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Start the development server
```bash
uvicorn app.main:app --reload

The API will be available at:
👉 http://127.0.0.1:8000


📚 API Documentation
Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

```

## 📁 Project Structure

```bash

E-COMMERCE/
├── app/
│ ├── auth/ # Handles authentication (JWT)
│ │ ├── init.py
│ │ ├── jwt_bearer.py # Defines JWTBearer dependency for protected routes
│ │ ├── jwt_handler.py # Creates and decodes JWT tokens
│ ├── crud/ # All CRUD operations for each module
│ │ ├── init.py
│ │ ├── carts.py
│ │ ├── orders.py
│ │ ├── products.py
│ │ ├── reviews.py
│ │ ├── users.py
│ ├── models/ # SQLAlchemy models for DB tables
│ │ ├── init.py
│ │ ├── cart.py
│ │ ├── order.py
│ │ ├── product.py
│ │ ├── review.py
│ │ ├── user.py
│ ├── routers/ # API endpoints/route definitions
│ │ ├── init.py
│ │ ├── carts.py
│ │ ├── orders.py
│ │ ├── products.py
│ │ ├── reviews.py
│ │ ├── users.py
│ ├── schemas/ # Pydantic schemas for request/response validation
│ │ ├── init.py
│ │ ├── cart.py
│ │ ├── order.py
│ │ ├── product.py
│ │ ├── review.py
│ │ ├── users.py
│ ├── init.py
│ ├── config.py # Configuration and settings (e.g., secret key, DB URL)
│ ├── database.py # DB connection using SQLAlchemy
│ ├── main.py # FastAPI app entry point
├── ecomerce.db # SQLite database file (can be replaced with other DB)
├── README.md # Project documentation
├── requirements.txt # Python dependencies
└── venv/ # Python virtual environment (optional - not pushed to Git)

```
---

## 🔗 API Endpoints

### Authentication
- `POST /users/register` – Register a new user
- `POST /users/login` – Login user
- `GET /users/me` – Get current user profile

### Products
- `GET /products/` – List all products
- `GET /products/{id}` – Get product by ID
- `POST /products/` – Create a product (admin only)
- `PUT /products/{id}` – Update product (admin only)
- `DELETE /products/{id}` – Delete product (admin only)

### Cart
- `GET /cart/` – Retrieve user cart
- `POST /cart/items` – Add item to cart
- `PUT /cart/items/{id}` – Update cart item quantity
- `DELETE /cart/items/{id}` – Remove cart item

### Orders
- `GET /orders/` – Get all user orders
- `POST /orders/` – Create a new order
- `GET /orders/{id}` – Get specific order details

### Reviews
- `GET /products/{id}/reviews` – Get product reviews
- `POST /products/{id}/reviews` – Submit a product review

---

## 🙋‍♂️ Support

If you have any questions or need help:

- 📖 Check the documentation
- 🐞 Open an issue
- 📬 Contact: trimalrao2004@gmail.com  


---

## 🗺️ Roadmap

- Payment gateway integration  
- Email notifications  
- Product image uploads  
- Advanced search with Elasticsearch  
- Rate limiting  
- API versioning  
- Admin dashboard  
- Mobile app API enhancements  

---

## 👨‍💻 Author

Your Name  
GitHub: [Ktrimalrao](https://github.com/Ktrimalrao)  
Email: trimalrao2004@gmail.com  
LinkedIn: [K Trimal Rao](https://www.linkedin.com/in/k-trimal-rao-397924253)  

---

## ⭐ Acknowledgments

- FastAPI – for the amazing framework  
- Pydantic – for elegant data validation  
- SQLAlchemy – for ORM capabilities  

Made with ❤️ using FastAPI
