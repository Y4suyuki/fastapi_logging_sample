from typing import Union
import logging

from fastapi import FastAPI

from .helper.util import foo

# from .helper.util import foo


app = FastAPI()

formatter = logging.Formatter('{"datetime": "%(asctime)s", "level": "%(levelname)s", "msg": "%(message)s"}')
local_formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()

if False:
    handler.setFormatter(local_formatter)
else:
    handler.setFormatter(formatter)

handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

@app.get("/")
def read_root():
    logger.warn("warn from root")
    logger.info("info from root")
    logger.debug("debug from root")
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    foo('a')
    return {"item_id": item_id, "q": q}

