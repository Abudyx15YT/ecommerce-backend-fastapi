from sqlalchemy.orm import Session
from ..models.review import Review
from ..schemas.review import ReviewCreate, ReviewUpdate

def get_review(db: Session, review_id: int):
    return db.query(Review).filter(Review.id == review_id).first()

def get_reviews_by_product(db: Session, product_id: int, skip: int = 0, limit: int = 100):
    return db.query(Review).filter(Review.product_id == product_id).offset(skip).limit(limit).all()

def get_reviews_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(Review).filter(Review.user_id == user_id).offset(skip).limit(limit).all()

def create_review(db: Session, review: ReviewCreate, user_id: int):
    db_review = Review(
        product_id=review.product_id,
        user_id=user_id,
        rating=review.rating,
        comment=review.comment
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def update_review(db: Session, review_id: int, review: ReviewUpdate, user_id: int):
    db_review = db.query(Review).filter(
        Review.id == review_id,
        Review.user_id == user_id
    ).first()
    
    if not db_review:
        return None
    
    update_data = review.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_review, key, value)
    
    db.commit()
    db.refresh(db_review)
    return db_review

def delete_review(db: Session, review_id: int, user_id: int):
    db_review = db.query(Review).filter(
        Review.id == review_id,
        Review.user_id == user_id
    ).first()
    
    if not db_review:
        return None
    
    db.delete(db_review)
    db.commit()
    return db_review