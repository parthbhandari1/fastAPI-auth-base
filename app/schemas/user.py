from pydantic import BaseModel, EmailStr

class OAuth2EmailPasswordRequestForm(BaseModel):
    email: EmailStr
    password: str

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    f_name: str
    l_name: str

class UserInDB(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
