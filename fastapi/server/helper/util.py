import logging

logger = logging.getLogger(__name__)


def foo():
    logger.info("hello from foo")
    return True
