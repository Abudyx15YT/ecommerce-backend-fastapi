from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from ..database import get_db
from ..schemas.product import Product, ProductCreate, ProductUpdate, Category, CategoryCreate, CategoryUpdate
from ..crud.products import (
    get_product, get_products, create_product, update_product, delete_product,
    get_category, get_categories, create_category, update_category, delete_category,
    search_products, get_product_by_sku
)
from ..auth.jwt_bearer import JWTBearer, get_current_admin_user

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

# Category endpoints
@router.post("/categories", response_model=Category)
def create_category_endpoint(
    category: CategoryCreate, 
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin_user)
):
    return create_category(db=db, category=category)

@router.get("/categories", response_model=List[Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = get_categories(db, skip=skip, limit=limit)
    return categories

@router.get("/categories/{category_id}", response_model=Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.put("/categories/{category_id}", response_model=Category)
def update_category_endpoint(
    category_id: int, 
    category: CategoryUpdate, 
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin_user)
):
    db_category = update_category(db, category_id, category)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.delete("/categories/{category_id}", response_model=Category)
def delete_category_endpoint(
    category_id: int, 
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin_user)
):
    db_category = delete_category(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

# Product endpoints
@router.post("/", response_model=Product)
def create_product_endpoint(
    product: ProductCreate, 
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin_user)
):
    # Check if category exists
    db_category = get_category(db, category_id=product.category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    
    # Check if SKU already exists
    db_product = get_product_by_sku(db, sku=product.sku)
    if db_product:
        raise HTTPException(status_code=400, detail="SKU already exists")
    
    return create_product(db=db, product=product)

@router.get("/", response_model=List[Product])
def read_products(
    skip: int = 0, 
    limit: int = 100, 
    category_id: Optional[int] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    if search:
        products = search_products(db, search, skip=skip, limit=limit)
    else:
        products = get_products(db, skip=skip, limit=limit, category_id=category_id)
    return products

@router.get("/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.put("/{product_id}", response_model=Product)
def update_product_endpoint(
    product_id: int, 
    product: ProductUpdate, 
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin_user)
):
    # Check if category exists if provided
    if product.category_id is not None:
        db_category = get_category(db, category_id=product.category_id)
        if db_category is None:
            raise HTTPException(status_code=404, detail="Category not found")
    
    db_product = update_product(db, product_id, product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.delete("/{product_id}", response_model=Product)
def delete_product_endpoint(
    product_id: int, 
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin_user)
):
    db_product = delete_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product