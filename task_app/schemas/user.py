from pydantic import BaseModel, validator, Field
import typing as t


class UserBase(BaseModel):
    username: str = Field("username", max_length=30, min_length=1)
    email: str = Field("email", max_length=30, min_length=1)
    password: str = Field("password", min_length=1)
    

class UserCreate(UserBase):
    pass
    
    class Config:
        orm_mode = True