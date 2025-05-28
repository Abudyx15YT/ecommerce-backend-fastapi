from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..schemas.cart import CartItem, CartItemCreate, CartItemUpdate, CartDisplay
from ..crud.carts import (
    get_cart_items, get_cart_item, create_cart_item, update_cart_item,
    delete_cart_item, clear_cart, calculate_cart_total
)
from ..crud.products import get_product
from ..auth.jwt_bearer import JWTBearer

router = APIRouter(
    prefix="/cart",
    tags=["cart"]
)

@router.get("/", response_model=CartDisplay)
def read_cart(current_user=Depends(JWTBearer()), db: Session = Depends(get_db)):
    cart_items = get_cart_items(db, user_id=current_user.id)
    total_price = calculate_cart_total(db, current_user.id)
    return {"items": cart_items, "total_price": total_price}

@router.post("/items", response_model=CartItem)
def add_to_cart(
    cart_item: CartItemCreate, 
    current_user=Depends(JWTBearer()), 
    db: Session = Depends(get_db)
):
    # Check if product exists
    product = get_product(db, product_id=cart_item.product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Check if product is in stock
    if product.stock_quantity < cart_item.quantity:
        raise HTTPException(status_code=400, detail="Not enough stock available")
    
    return create_cart_item(db=db, cart_item=cart_item, user_id=current_user.id)

@router.put("/items/{cart_item_id}", response_model=CartItem)
def update_cart_item_endpoint(
    cart_item_id: int, 
    cart_item: CartItemUpdate, 
    current_user=Depends(JWTBearer()), 
    db: Session = Depends(get_db)
):
    # Get the cart item
    db_cart_item = get_cart_item(db, cart_item_id=cart_item_id, user_id=current_user.id)
    if not db_cart_item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    
    # Check if product has enough stock
    product = get_product(db, product_id=db_cart_item.product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    if product.stock_quantity < cart_item.quantity:
        raise HTTPException(status_code=400, detail="Not enough stock available")
    
    return update_cart_item(db, cart_item_id, cart_item, current_user.id)

@router.delete("/items/{cart_item_id}", response_model=CartItem)
def remove_from_cart(
    cart_item_id: int, 
    current_user=Depends(JWTBearer()), 
    db: Session = Depends(get_db)
):
    db_cart_item = delete_cart_item(db, cart_item_id, current_user.id)
    if not db_cart_item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    return db_cart_item

@router.delete("/clear")
def clear_cart_endpoint(current_user=Depends(JWTBearer()), db: Session = Depends(get_db)):
    clear_cart(db, current_user.id)
    return {"message": "Cart cleared successfully"}