# Example: Basic and Advanced Logging Configuration

import logging


# Create junior logger
logger = logging.getLogger('test')

# Set the formatter for the child logger
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Log junior message from the child logger
logger.info('INFO message from the child logger')
