from sqlalchemy.orm import Session
from models.task import Task as TaskModel
from models.user import User as UserModel
import schemas.task as task_schema
from typing import List, Optional


def get_tasks(db: Session, user_id: int) -> Optional[List[TaskModel]]:
    tasks = db.query(TaskModel).filter(TaskModel.user_id == user_id).all()
    # リレーションを貼るとこうすることもできる
    # user = db.query(UserModel).filter(UserModel.id == user_id).first()
    # tasks = user.tasks
    # joinするとこうなる
    # tasks = db.query(TaskModel).join(UserModel).filter(UserModel.id == user_id).all()
    return tasks


def get_task(db: Session, id: int) -> Optional[TaskModel]:
    return db.query(TaskModel).filter(TaskModel.id == id).first()


def create_task(db: Session, task_create: task_schema.TaskCreate, user_id: int) -> TaskModel:
    task = TaskModel(title=task_create.title,
                     content=task_create.content, user_id=user_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def update_task(db: Session, id: int, task_update: task_schema.TaskUpdate) -> Optional[TaskModel]:
    task = db.query(TaskModel).filter(TaskModel.id == id).first()
    if task:
        task.title = task_update.title
        task.content = task_update.content
        db.commit()
        db.refresh(task)
        return task
    return None


def delete_task(db: Session, id: int) -> Optional[TaskModel]:
    task = db.query(TaskModel).filter(TaskModel.id == id).first()
    if task:
        db.delete(task)
        db.commit()
        return task
    return None
