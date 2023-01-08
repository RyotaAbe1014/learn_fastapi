from fastapi import FastAPI
from routers import task


app = FastAPI()
app.include_router(task.router)


@app.get("/")
async def hello():
    return {"message": "hello world"}
