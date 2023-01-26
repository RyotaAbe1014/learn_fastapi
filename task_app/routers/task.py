from fastapi import APIRouter, Path, Depends
from typing import List
import schemas.task as TaskSchema
import cruds.task as crud
from db import session
from settings.custom_route import CustomRoute
from auth.oauth2 import oauth2_scheme

router = APIRouter(prefix="/tasks", tags=["tasks"], route_class=CustomRoute)


@router.get("/", response_model=List[TaskSchema.Task])
async def list_tasks(token: str = Depends(oauth2_scheme)):
    return crud.get_tasks(session)


@router.post("/", response_model=TaskSchema.Task)
async def create_task(task: TaskSchema.TaskCreate, token: str = Depends(oauth2_scheme)):
    return crud.create_task(session, task)


@router.get("/{task_id}", response_model=TaskSchema.Task)
async def detail_task(task_id: int = Path(..., description="タスクID"), token: str = Depends(oauth2_scheme)):
    return crud.get_task(session, task_id)


@router.put("/{task_id}", response_model=TaskSchema.Task)
async def update_task(task: TaskSchema.TaskUpdate, task_id: int = Path(..., description="タスクID"), token: str = Depends(oauth2_scheme)):
    return crud.update_task(session, task_id, task)


@router.delete("/{task_id}",  response_model=TaskSchema.Task)
async def delete_task(task_id: int = Path(..., description="タスクID"), token: str = Depends(oauth2_scheme)):
    return crud.delete_task(session, task_id)
