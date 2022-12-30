from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# モデルのベースクラス
Base = declarative_base()

# モデルクラス


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    tasks = relationship('Task', back_populates='user')


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(
        "users.id", onupdate='CASCADE', ondelete='CASCADE'))
    title = Column(String)
    user = relationship('User', back_populates='tasks')


# back_populatesパラメータを使用することで、双方向のリレーションを張ることができる
# UserモデルクラスからTaskモデルクラスを参照するtasksリレーションと
# TaskモデルクラスからTaskモデルクラスを参照するuserリレーションを同時に張っています。
