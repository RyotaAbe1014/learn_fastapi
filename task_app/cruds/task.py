from sqlalchemy.orm import Session
from models.task import Task
from schemas.task import TaskCreate
from typing import List, Optional


def get_tasks(db: Session) -> Optional[List[Task]]:
    return db.query(Task).all()


def get_task(db: Session, id: int) -> Optional[Task]:
    return db.query(Task).filter(Task.id == id).first()


def create_task(db: Session, task_schema: TaskCreate):
    pass
