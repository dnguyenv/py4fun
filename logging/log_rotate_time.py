import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# s, m, h, d, midnight, w0, w1

handler = TimedRotatingFileHandler('time_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)
for _ in range(10):
    logger.info('Hello world')
    time.sleep(5)