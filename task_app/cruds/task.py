from sqlalchemy.orm import Session
from models.task import Task
import schemas.task


def get_tasks(db: Session):
    return db.query(Task).all()


def get_task(db: Session, id: int):
    return db.query(Task).filter(Task.id == id).first()


