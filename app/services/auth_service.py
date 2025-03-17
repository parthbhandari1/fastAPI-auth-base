from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserInDB
from app.models.user import User
from app.core.security import get_password_hash, verify_password
from pydantic import EmailStr


class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def signup_user(self, user: UserCreate) -> UserInDB:
        # Check if the user already exists
        existing_user = self.get_user_by_email_from_db(user.email)
        if existing_user:
            raise ValueError("Email already registered")

        # Create the user
        db_user = self.create_user(user)
        return UserInDB(id=db_user.id, email=db_user.email)

    def authenticate_user(self, email: EmailStr, password: str):
        # Authenticate the user
        user = self.authenticate_user_and_verify_password(email, password)
        if not user:
            raise ValueError("Incorrect email or password")
        return user

    def get_user_by_email(self, email: EmailStr):
        # Retrieve a user by email
        user = self.get_user_by_email_from_db(email)
        if not user:
            raise ValueError("User not found")
        return user

    def get_user_by_email_from_db(self, email: EmailStr):
        return self.db.query(User).filter(User.email == email).first()

    def create_user(self, user: UserCreate):
        hashed_password = get_password_hash(user.password)
        db_user = User(email=user.email, f_name=user.f_name, l_name=user.l_name, hashed_password=hashed_password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def authenticate_user_and_verify_password(self, email: EmailStr, password: str):
        user = self.get_user_by_email_from_db(email)
        if not user or not verify_password(password, user.hashed_password):
            return False
        return user
