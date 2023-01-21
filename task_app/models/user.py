from sqlalchemy import Boolean, Column, Integer, String, Text
from sqlalchemy.orm import relationship
from db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30))
    email = Column(String(30), unique=True)
    password = Column(String(255))
    is_active = Column(Boolean, default=True)
