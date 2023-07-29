import logging.config

logging.config.fileConfig('logging.conf')

logger = logging.getLogger('simpleExample')

logger.debug('this is a debug message')

# #logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s -%(message)s',
#                     datefmt='%m/%d/%Y %H:%M:%S')
#
# import helper
#
#
# logging.debug('this is debug message')
#
# logging.info('this is info message')
#
# logging.warning('this is warning message')
#
# logging.error('this is error message')
#
# logging.critical('this is critical message')