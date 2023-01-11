from fastapi import FastAPI
from settings.custom_route import CustomRoute
from routers import task

app = FastAPI()
app.router.route_class = CustomRoute
app.include_router(task.router)


@app.get("/")
async def hello():
    return {"message": "hello world"}
