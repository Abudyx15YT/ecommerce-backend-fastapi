from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import engine
from .models import user, product, order, cart, review
from .routers import users, products, orders, carts, reviews

# Create tables
user.Base.metadata.create_all(bind=engine)
product.Base.metadata.create_all(bind=engine)
order.Base.metadata.create_all(bind=engine)
cart.Base.metadata.create_all(bind=engine)
review.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-commerce API",
    description="API for E-commerce application built with FastAPI",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router)
app.include_router(products.router)
app.include_router(carts.router)
app.include_router(reviews.router)
app.include_router(orders.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the E-commerce API"}