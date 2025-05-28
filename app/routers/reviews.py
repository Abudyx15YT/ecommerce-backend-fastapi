from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..schemas.review import Review, ReviewCreate, ReviewUpdate
from ..crud.reviews import (
    get_review, get_reviews_by_product, get_reviews_by_user,
    create_review, update_review, delete_review
)
from ..crud.products import get_product
from ..auth.jwt_bearer import JWTBearer, get_current_admin_user

router = APIRouter(
    prefix="/reviews",
    tags=["reviews"]
)

@router.post("/", response_model=Review)
def create_review_endpoint(
    review: ReviewCreate, 
    current_user=Depends(JWTBearer()), 
    db: Session = Depends(get_db)
):
    # Check if product exists
    product = get_product(db, product_id=review.product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return create_review(db=db, review=review, user_id=current_user.id)

@router.get("/products/{product_id}", response_model=List[Review])
def read_product_reviews(
    product_id: int, 
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    # Check if product exists
    product = get_product(db, product_id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    reviews = get_reviews_by_product(db, product_id=product_id, skip=skip, limit=limit)
    return reviews

@router.get("/users/me", response_model=List[Review])
def read_user_reviews(
    skip: int = 0, 
    limit: int = 100, 
    current_user=Depends(JWTBearer()), 
    db: Session = Depends(get_db)
):
    reviews = get_reviews_by_user(db, user_id=current_user.id, skip=skip, limit=limit)
    return reviews

@router.put("/{review_id}", response_model=Review)
def update_review_endpoint(
    review_id: int, 
    review: ReviewUpdate, 
    current_user=Depends(JWTBearer()), 
    db: Session = Depends(get_db)
):
    db_review = update_review(db, review_id, review, current_user.id)
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found or you don't have permission to update it")
    return db_review

@router.delete("/{review_id}", response_model=Review)
def delete_review_endpoint(
    review_id: int, 
    current_user=Depends(JWTBearer()), 
    db: Session = Depends(get_db)
):
    db_review = delete_review(db, review_id, current_user.id)
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found or you don't have permission to delete it")
    return db_review