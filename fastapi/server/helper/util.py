import logging

logger = logging.getLogger(__name__)


def foo(x):
    logger.info("hello from foo")
    return x
