from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..schemas.order import Order, OrderCreate, OrderUpdate, OrderStatus
from ..crud.orders import (
    get_order, get_orders_by_user, get_orders,
    create_order, update_order_status, update_payment_status
)
from ..crud.carts import get_cart_items, calculate_cart_total
from ..auth.jwt_bearer import JWTBearer, get_current_admin_user

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

@router.post("/", response_model=Order)
def create_order_endpoint(
    order: OrderCreate, 
    current_user=Depends(JWTBearer()), 
    db: Session = Depends(get_db)
):
    # Check if cart is not empty
    cart_items = get_cart_items(db, user_id=current_user.id)
    if not cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty")
    
    # Check if there's a total amount in cart
    cart_total = calculate_cart_total(db, current_user.id)
    if cart_total <= 0:
        raise HTTPException(status_code=400, detail="Invalid cart total")
    
    return create_order(db=db, order=order, user_id=current_user.id)

@router.get("/my-orders", response_model=List[Order])
def read_user_orders(
    skip: int = 0, 
    limit: int = 100, 
    current_user=Depends(JWTBearer()), 
    db: Session = Depends(get_db)
):
    orders = get_orders_by_user(db, user_id=current_user.id, skip=skip, limit=limit)
    return orders

@router.get("/my-orders/{order_id}", response_model=Order)
def read_user_order(
    order_id: int, 
    current_user=Depends(JWTBearer()), 
    db: Session = Depends(get_db)
):
    order = get_order(db, order_id=order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    # Ensure the order belongs to the current user
    if order.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to view this order")
    
    return order

@router.get("/", response_model=List[Order])
def read_orders(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin_user)
):
    orders = get_orders(db, skip=skip, limit=limit)
    return orders

@router.get("/{order_id}", response_model=Order)
def read_order_admin(
    order_id: int, 
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin_user)
):
    order = get_order(db, order_id=order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.put("/{order_id}/status", response_model=Order)
def update_order_status_endpoint(
    order_id: int, 
    status: OrderStatus, 
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin_user)
):
    order = update_order_status(db, order_id, status)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.put("/{order_id}/payment", response_model=Order)
def update_payment_status_endpoint(
    order_id: int, 
    payment_status: str, 
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin_user)
):
    order = update_payment_status(db, order_id, payment_status)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order