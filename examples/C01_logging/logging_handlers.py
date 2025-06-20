# Multiple Logging Handlers
# ------------------------------------------------------------------------------
# Sets up stream, file and timed rotating handlers.

import logging.handlers
import time

# Advanced Handlers
handlers = [

    # logging.handlers.RotatingFileHandler(
    #     filename='test.log',
    #     maxBytes=10,
    #     backupCount=5
    # ),

    logging.StreamHandler(),
    logging.FileHandler('child.log'),

    logging.handlers.TimedRotatingFileHandler(
        filename='test.log',
        when='s',
        interval=5,
        backupCount=5
    )
]

logger = logging.getLogger('advanced_logger')

# Configure the child logger handlers
for handler in handlers:
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)

for i in range(10):
    logger.info('INFO message from the child logger')
    time.sleep(1)
