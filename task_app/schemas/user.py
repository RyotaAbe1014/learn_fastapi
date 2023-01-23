from pydantic import BaseModel, validator, Field
import typing as t
import re


class UserBase(BaseModel):
    username: str = Field("username", max_length=30, min_length=1)
    email: str = Field("email", max_length=30, min_length=1)
    password: str = Field("password", min_length=1)


class UserCreate(UserBase):

    @validator("username")
    def only_alphanumeric(cls, v):
        if not re.match("^[a-zA-Z0-9]+$", v):
            raise ValueError("英数字のみです")
        return v

    @validator("email")
    def validate_email(cls, v):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", v):
            raise ValueError("メールアドレスの形式が正しくありません")
        return v

    @validator("password")
    def password_must_contain_at_least_one_number(cls, v):
        if not any(char.isdigit() for char in v):
            raise ValueError("１つ以上の数字を含めてください")
        return v

    @validator("password")
    def password_must_contain_at_least_one_uppercase(cls, v):
        if not any(char.isupper() for char in v):
            raise ValueError("1つ以上の大文字を含めてください")
        return v

    class Config:
        orm_mode = True
