from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# モデルのベースクラス
Base = declarative_base()

# モデルクラス
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)