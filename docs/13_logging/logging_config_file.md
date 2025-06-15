# logging_config_file

```python
# Configuring Logging from a File
# --------------------------------------------------------------------------------
# Loads logger settings from an external configuration file.

import logging.config

# Configure the logging module with a configuration file
logging.config.fileConfig('logging.conf')

# Get the root logger instance
root = logging.getLogger()

# Check the logger dictionary
root.info(f"After fileConfig(): {logging.Logger.manager.loggerDict} ")

# Get the test logger instance
test = logging.getLogger('test')

# Check the logger dictionary
root.info(f"After getLogger('test'): {logging.Logger.manager.loggerDict} ")

# Log a message from the test logger
test.info('INFO message from the test logger')
```
