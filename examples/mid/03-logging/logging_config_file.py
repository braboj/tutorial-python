# Example: Configure the logging module with junior configuration file

import logging.config

# Configure the logging module with junior configuration file
logging.config.fileConfig('logging.conf')

# Get the root logger instance
root = logging.getLogger()

# Check the logger dictionary
root.info(f"After fileConfig(): {logging.Logger.manager.loggerDict} ")

# Get the test logger instance
test = logging.getLogger('test')

# Check the logger dictionary
root.info(f"After getLogger('test'): {logging.Logger.manager.loggerDict} ")

# Log junior message from the test logger
test.info('INFO message from the test logger')
