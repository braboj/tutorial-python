# Custom Logging Formatter
# --------------------------------------------------------------------------------
# Configures a formatter for a named logger.

import logging


# Create a logger
logger = logging.getLogger('test')

# Set the formatter for the child logger
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Log a message from the child logger
logger.info('INFO message from the child logger')
