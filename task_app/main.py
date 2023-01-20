from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from settings.custom_route import CustomRoute
from routers import task
from pydantic import BaseModel


app = FastAPI()
app.router.route_class = CustomRoute


@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    """
    カスタムエラーハンドリング
    コメントを外すと、認証が必要なエンドポイントにアクセスすると
    FastAPIよりも先に401が返る
    """
    if request.url.path.startswith("/docs") or request.url.path.startswith("/redoc") or request.url.path.startswith("/openapi.json") :
        "openAPIドキュメントでは401を返すようにすると、ドキュメントそのものが開けなくなる対応"
        response = await call_next(request)
        return response
    if not request.headers.get("Authorization"):
        return JSONResponse(content={"message": "Not authorized"}, status_code=401)
    response = await call_next(request)
    return response

app.include_router(task.router)


"""
実験用
"""


class Message(BaseModel):
    message: str


@app.post("/")
async def hello(message: Message):
    return {"message": message.message}
