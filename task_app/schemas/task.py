from pydantic import BaseModel
import typing as t


class TaskBase(BaseModel):
    title: str
    content: t.Optional[str]


class TaskCreate(TaskBase):
    class Config:
        orm_mode = True


class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True