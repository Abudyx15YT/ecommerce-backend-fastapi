from pydantic import BaseModel, validator, Field
from typing import Optional, List, Union
from datetime import datetime

class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None
    parent_id: Optional[int] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    parent_id: Optional[int] = None

class Category(CategoryBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class ProductImageBase(BaseModel):
    image_url: str
    is_primary: bool = False

class ProductImageCreate(ProductImageBase):
    pass

class ProductImage(ProductImageBase):
    id: int
    product_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float = Field(..., gt=0)
    discount_amount: float = 0
    stock_quantity: int = 0
    sku: str
    category_id: int
    is_active: bool = True

    @validator('price')
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Price must be greater than 0')
        return v
    
    @validator('discount_amount')
    def discount_must_not_exceed_price(cls, v, values):
        if 'price' in values and v > values['price']:
            raise ValueError('Discount amount cannot exceed price')
        return v

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    discount_amount: Optional[float] = None
    stock_quantity: Optional[int] = None
    category_id: Optional[int] = None
    is_active: Optional[bool] = None

class Product(ProductBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    images: List[ProductImage] = []
    category: Category

    class Config:
        orm_mode = True

class ProductWithReviews(Product):
    average_rating: Optional[float] = None
    review_count: int = 0