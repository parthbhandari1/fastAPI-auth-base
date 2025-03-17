from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.security import create_access_token
from app.services.auth_service import AuthService
from app.schemas.user import OAuth2EmailPasswordRequestForm, UserCreate, UserInDB, Token
from app.db.session import get_db

router = APIRouter()

@router.post("/signup", response_model=UserInDB)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    try:
        user_in_db = auth_service.signup_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return user_in_db

@router.post("/login", response_model=Token)
def login(form_data: OAuth2EmailPasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    try:
        user = auth_service.authenticate_user(form_data.email, form_data.password)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
