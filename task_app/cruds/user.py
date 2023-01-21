from sqlalchemy.orm import Session
from models.user import User as UserModel
import schemas.user as UserSchema
from typing import List, Optional
from auth.hash import Hash


# def create_task(db: Session, task_create: task_schema.TaskCreate) -> TaskModel:
#     task = TaskModel(title=task_create.title, content=task_create.content)
#     db.add(task)
#     db.commit()
#     db.refresh(task)
#     return task


def create_user(db: Session, user_create: UserSchema.UserCreate) -> UserModel:
    user = UserModel(
        username=user_create.username,
        email=user_create.email,
        password=Hash.get_password_hash(user_create.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
