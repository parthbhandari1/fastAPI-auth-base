from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings

# Password hashing setup using passlib
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# JWT Token creation and validation
def create_access_token(data: dict) -> str:
    """
    Create a JWT access token.
    :param data: The data to encode in the JWT.
    :return: A JWT token as a string.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against a hashed password.
    :param plain_password: The password input from the user.
    :param hashed_password: The stored hashed password in the database.
    :return: True if passwords match, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Hash a plain password using bcrypt.
    :param password: The plain password to hash.
    :return: The hashed password.
    """
    return pwd_context.hash(password)


# def verify_jwt_token(token: str) -> dict:
#     """
#     Verify the JWT token and decode it.
#     :param token: The JWT token to verify.
#     :return: The decoded token data if valid, raises an exception otherwise.
#     """
#     try:
#         payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
#         return payload
#     except jwt.ExpiredSignatureError:
#         raise Exception("Token has expired")
#     except jwt.JWTError:
#         raise Exception("Invalid token")
