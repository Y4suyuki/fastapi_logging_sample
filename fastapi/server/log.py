import contextvars
from typing import Union
import logging
import logging.config
from os import path


log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')

request_id_context = contextvars.ContextVar[Union[str, None]]("request_id", default=None)

logging.config.fileConfig(log_file_path, disable_existing_loggers=False)
logger = logging.getLogger('production')
reqres_logger = logging.getLogger('productionReqRes')

class RequestIdFilter(logging.Filter):
    def filter(self, record):
        record.request_id = request_id_context.get()
        return True

logger.addFilter(RequestIdFilter())
reqres_logger.addFilter(RequestIdFilter())
