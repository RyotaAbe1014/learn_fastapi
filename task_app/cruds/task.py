from sqlalchemy.orm import Session
from models.task import Task as TaskModel
import schemas.task as task_schema
from typing import List, Optional


def get_tasks(db: Session) -> Optional[List[TaskModel]]:
    return db.query(TaskModel).all()


def get_task(db: Session, id: int) -> Optional[TaskModel]:
    return db.query(TaskModel).filter(TaskModel.id == id).first()


def create_task(db: Session, task_create: task_schema.TaskCreate) -> TaskModel:
    task = TaskModel(title=task_create.title, content=task_create.content)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task
