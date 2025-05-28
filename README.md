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

app/
├── main.py              # FastAPI app initialization
├── config.py            # Configuration settings
├── database.py          # Database connection
├── models/              # SQLAlchemy models
│   ├── __init__.py
│   ├── user.py
│   ├── product.py
│   ├── cart.py
│   ├── order.py
│   └── review.py
├── schemas/             # Pydantic schemas
│   ├── __init__.py
│   ├── users.py
│   ├── product.py
│   ├── cart.py
│   ├── order.py
│   └── review.py
├── routers/             # API routes
│   ├── __init__.py
│   ├── users.py
│   ├── products.py
│   ├── carts.py
│   ├── orders.py
│   └── reviews.py
├── auth/                # Authentication logic
│   ├── __init__.py
│   └── jwt_handler.py
└── utils/               # Utility functions
    ├── __init__.py
    └── helpers.py


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
- 📬 Contact: your-email@example.com

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
LinkedIn: [K Trimal Rao](www.linkedin.com/in/k-trimal-rao-397924253)  

---

## ⭐ Acknowledgments

- FastAPI – for the amazing framework  
- Pydantic – for elegant data validation  
- SQLAlchemy – for ORM capabilities  

Made with ❤️ using FastAPI