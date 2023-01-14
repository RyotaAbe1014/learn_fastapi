from fastapi import APIRouter
from typing import List
import schemas.task as TaskSchema
import cruds.task as crud
from db import session
from settings.custom_route import CustomRoute
router = APIRouter(prefix="/tasks", tags=["tasks"])
router.route_class = CustomRoute


@router.get("/", response_model=List[TaskSchema.Task])
async def list_tasks():
    return crud.get_tasks(session)


@router.post("/", response_model=TaskSchema.Task)
async def create_task(task: TaskSchema.TaskCreate):
    return crud.create_task(session, task)


@router.get("/{task_id}", response_model=TaskSchema.Task)
async def detail_task(task_id: int):
    return crud.get_task(session, task_id)


@router.put("/{task_id}", response_model=TaskSchema.Task)
async def update_task(task: TaskSchema.TaskUpdate, task_id: int):
    return crud.update_task(session, task_id, task)


@router.delete("/{task_id}",  response_model=TaskSchema.Task)
async def delete_task(task_id: int):
    return crud.delete_task(session, task_id)
