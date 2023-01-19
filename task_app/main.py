from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from settings.custom_route import CustomRoute
from routers import task
from pydantic import BaseModel


app = FastAPI()
app.router.route_class = CustomRoute


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        content={"message": exc.detail},
        status_code=exc.status_code
    )


@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    """
    カスタムエラーハンドリング
    コメントを外すと、認証が必要なエンドポイントにアクセスすると
    FastAPIよりも先に401が返る
    """
    # if not request.headers.get("Authorization"):
    #     return JSONResponse(content={"message": "Not authorized"}, status_code=401)
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
