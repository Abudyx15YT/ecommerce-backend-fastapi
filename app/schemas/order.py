from pydantic import BaseModel, Field
from typing import List, Optional, Union
from datetime import datetime
from enum import Enum

class OrderStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class PaymentStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    FAILED = "failed"
    REFUNDED = "refunded"

class OrderItemBase(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)
    price: float
    discount_amount: float = 0

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)

class OrderItem(OrderItemBase):
    id: int
    order_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class OrderItemWithProduct(OrderItem):
    product_name: str
    product_sku: str
    
    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    shipping_address: str
    billing_address: Optional[str] = None

class OrderCreate(OrderBase):
    items: List[OrderItemCreate]

class OrderUpdate(BaseModel):
    status: Optional[OrderStatus] = None
    payment_status: Optional[PaymentStatus] = None
    tracking_number: Optional[str] = None

class PaymentBase(BaseModel):
    payment_method: str
    transaction_id: Optional[str] = None
    amount: float

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int
    order_id: int
    status: PaymentStatus
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class Order(BaseModel):
    id: int
    user_id: Optional[int] = None
    total_amount: float
    status: OrderStatus
    payment_status: PaymentStatus
    tracking_number: Optional[str] = None
    shipping_address: str
    billing_address: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    items: List[OrderItemWithProduct] = []
    payment: Optional[Payment] = None

    class Config:
        orm_mode = True
