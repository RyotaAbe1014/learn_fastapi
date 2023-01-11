from fastapi import FastAPI, Request, Response
from routers import task
import time
import datetime
import sys
import json
from logging import getLogger, StreamHandler, DEBUG
from typing import Callable
from fastapi.routing import APIRoute

logger = getLogger(__name__)
handler = StreamHandler(sys.stdout)
handler.setLevel(DEBUG)
logger.addHandler(handler)
logger.setLevel(DEBUG)


class CustomRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            """
            時間計測
            """
            before = time.time()
            response: Response = await original_route_handler(request)
            record = {}
            time_local = datetime.datetime.fromtimestamp(before)
            record["time_local"] = time_local.strftime("%Y/%m/%d %H:%M:%S%Z")
            if await request.body():
                record["request_body"] = (await request.body()).decode("utf-8")
            record["request_headers"] = {
                k.decode("utf-8"): v.decode("utf-8") for (k, v) in request.headers.raw
            }
            record["remote_addr"] = request.client.host
            record["request_uri"] = request.url.path
            record["request_method"] = request.method
            record["status"] = response.status_code
            record["response_body"] = response.body.decode("utf-8")
            record["response_headers"] = {
                k.decode("utf-8"): v.decode("utf-8") for (k, v) in response.headers.raw
            }
            logger.info(json.dumps(record))
            return response

        return custom_route_handler


app = FastAPI()
app.router.route_class = CustomRoute
app.include_router(task.router)


@app.get("/")
async def hello():
    return {"message": "hello world"}
