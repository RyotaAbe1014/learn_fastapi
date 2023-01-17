from sqlalchemy import Boolean, Column, Integer, String, 

from db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30))
    email = Column(String(30), unique=True, index=True)
    password = Column(String(255))
    is_active = Column(Boolean, default=True)
    # tasks = relationship("Task", back_populates="owner")