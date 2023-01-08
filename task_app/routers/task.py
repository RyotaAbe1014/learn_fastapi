from fastapi import APIRouter, Depends
from typing import List
from schemas.task import Task as TaskSchema
from cruds.task import get_tasks
from db import session

router = APIRouter()


@router.get("/tasks", response_model=List[TaskSchema])
async def list_tasks():
    return get_tasks(session)


@router.post("/tasks")
async def create_task():
    pass


@router.put("/tasks/{task_id}")
async def update_task():
    pass


@router.delete("/tasks/{task_id}")
async def delete_task():
    pass
