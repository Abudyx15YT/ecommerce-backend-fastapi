from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .jwt_handler import verify_token
from sqlalchemy.orm import Session
from ..database import get_db
from ..crud.users import get_user_by_username

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request, db: Session = Depends(get_db)):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            
            credentials_exception = HTTPException(
                status_code=401,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
            token_data = verify_token(credentials.credentials, credentials_exception)
            user = get_user_by_username(db, token_data.username)
            if not user:
                raise credentials_exception
            return user
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

# Dependency for admin users
def get_current_admin_user(current_user=Depends(JWTBearer())):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return current_user