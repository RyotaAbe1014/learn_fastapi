from fastapi import APIRouter
from typing import List
from schemas.task import Task as TaskSchema
from cruds.task import get_tasks, get_task
from db import session

router = APIRouter()


@router.get("/tasks", response_model=List[TaskSchema])
async def list_tasks():
    return get_tasks(session)


@router.post("/tasks")
async def create_task():
    pass


@router.get("/tasks/{task_id}", response_model=TaskSchema)
async def detail_task(id: int):
    return get_task(session, id)
    

@router.put("/tasks/{task_id}")
async def update_task():
    pass


@router.delete("/tasks/{task_id}")
async def delete_task():
    pass
