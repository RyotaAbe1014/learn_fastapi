from sqlalchemy.orm import Session
from models.task import Task
from schemas.task import Task as t


def get_tasks(db: Session):
    return db.query(Task).all()
