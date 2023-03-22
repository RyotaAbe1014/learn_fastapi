import requests
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()


def run_task():
    # 非同期処理
    pass




@app.post("/tasks")
async def create_task(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_task) # 非同期処理
    return {"message": "Task created"}