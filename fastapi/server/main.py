from typing import Any, Callable, Coroutine, Union
from uuid import uuid4

from fastapi import FastAPI, Response, Request
from fastapi.routing import APIRoute
from pydantic import BaseModel

from .helper.util import foo
from .log import logger, reqres_logger, request_id_context


class LoggingRoute(APIRoute):
    def get_route_handler(self) -> Callable[[Request], Coroutine[Any, Any, Response]]:
        original_route_handler = super().get_route_handler()
        async def custom_route_handler(request: Request) -> Response:
            response = await original_route_handler(request)
            b_request_body = await request.body()
            request_body = b_request_body.decode('utf8')
            response_body = response.body.decode('utf8')
            reqres_logger.info("request and response body", extra={"request": request_body, "response": response_body}) 
            return response

        return custom_route_handler


# App initialize
app = FastAPI()
app.router.route_class = LoggingRoute


@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request_id = str(uuid4())
    request_id_context.set(request_id)
    response = await call_next(request)
    return response


# Models
class Item(BaseModel):
    name: str
    item_id: str


# Handlers
@app.get("/")
def read_root():
    logger.warn("warn from root")
    logger.info("info from root")
    logger.debug("debug from root")
    return {"Hello": "World"}


@app.post("/examine")
def examine(item: Item):
    return item


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    foo('a')
    return {"item_id": item_id, "q": q}
