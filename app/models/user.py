from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    f_name = Column(String)
    l_name = Column(String)
    hashed_password = Column(String)
    is_seller = Column(Boolean, default=False)
