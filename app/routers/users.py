from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import timedelta

from ..database import get_db
from ..schemas.users import User, UserCreate, UserUpdate


from ..crud.users import (
    get_user, get_users, create_user, update_user, delete_user,
    get_user_by_email, get_user_by_username, authenticate_user
)
from ..auth.jwt_handler import create_access_token
from ..auth.jwt_bearer import JWTBearer, get_current_admin_user
from ..config import settings

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/register", response_model=User)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user_email = get_user_by_email(db, email=user.email)
    if db_user_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    db_user_username = get_user_by_username(db, username=user.username)
    if db_user_username:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    return create_user(db=db, user=user)

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(db, username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=User)
def read_users_me(current_user=Depends(JWTBearer())):
    return current_user

@router.put("/me", response_model=User)
def update_user_me(user: UserUpdate, current_user=Depends(JWTBearer()), db: Session = Depends(get_db)):
    return update_user(db, current_user.id, user)

@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/", response_model=List[User])
def read_users(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin_user)
):
    users = get_users(db, skip=skip, limit=limit)
    return users

@router.put("/{user_id}", response_model=User)
def update_user_admin(
    user_id: int, 
    user: UserUpdate, 
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin_user)
):
    db_user = update_user(db, user_id, user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{user_id}", response_model=User)
def delete_user_endpoint(
    user_id: int, 
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin_user)
):
    db_user = delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user