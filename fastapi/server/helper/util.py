from ..log import logger


def foo(x):
    logger.info("hello from foo")
    logger.info(__name__)
    return x
