from typing import Union
import logging

from fastapi import FastAPI

from .helper.util import foo


app = FastAPI()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@app.get("/")
def read_root():
    logger.warn("warn from root")
    logger.info("info from root")
    logger.debug("debug from root")
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    foo()
    return {"item_id": item_id, "q": q}

