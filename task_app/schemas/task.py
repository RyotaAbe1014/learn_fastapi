from pydantic import BaseModel, validator
import typing as t


class TaskBase(BaseModel):
    title: str
    content: t.Optional[str]

    @validator("title")
    def check_title_length(cls, value):
        if len(value) > 30:
            raise ValueError("titleは30文字以内で入力してください。")
        return value

    @validator("content")
    def check_content_length(cls, value):
        if len(value) > 255:
            raise ValueError("contentは255文字以内で入力してください。")
        return value


class TaskCreate(TaskBase):
    class Config:
        orm_mode = True


class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True


class TaskUpdate(Task):
    pass


class TaskDelete(Task):
    pass
