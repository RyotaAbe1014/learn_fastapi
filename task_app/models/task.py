
from sqlalchemy import Boolean, Column, Integer, String

from db import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(30))
    content = Column(String, nullable=True)
