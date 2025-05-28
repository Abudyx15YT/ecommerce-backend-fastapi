from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class CartItemBase(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    quantity: int = Field(..., gt=0)

class CartItem(CartItemBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class CartItemWithProduct(CartItem):
    product_name: str
    product_price: float
    product_discount: float
    product_image: Optional[str] = None
    
    class Config:
        orm_mode = True

class CartSummary(BaseModel):
    items: List[CartItemWithProduct]
    total_items: int
    subtotal: float
    total_discount: float
    total: float

class CartDisplay(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    # Add any other fields that should be displayed to the user
    
    class Config:
        from_attributes = True 