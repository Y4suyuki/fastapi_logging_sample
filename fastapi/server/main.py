from typing import Union
import logging
import logging.config

from fastapi import FastAPI

from .helper.util import foo
from os import path
log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')

# from .helper.util import foo
app = FastAPI()


logging.config.fileConfig(log_file_path)
logger = logging.getLogger('production')


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

