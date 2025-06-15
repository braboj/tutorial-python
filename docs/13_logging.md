# Logging

## Logging Advanced Config

```python
# Advanced Logging Configuration
# --------------------------------------------------------------------------------
# Demonstrates custom handlers, a formatter, and propagation control.

import logging

# Root logger configuration
logging.basicConfig(level=logging.DEBUG)

# Create the root logger (no name is provided)
root = logging.getLogger()
root.setLevel(logging.DEBUG)
root.debug('DEBUG message from the root logger')

# Create a child logger (name is provided)
child = logging.getLogger('child')

# Set the formatter for the child logger
child_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Configure the child logger handlers (file and console)
child_handlers = [
    logging.FileHandler('child.log'),
    logging.StreamHandler(),
]

# Configure the child logger handlers
for handler in child_handlers:
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(child_formatter)
    child.addHandler(handler)

# Enable/Diable propagation of the child logger messages to the root logger
child.propagate = False

# Log a message from the child logger
child.info('INFO message from the child logger')
```

## Logging Basic Config

```python
# Basic Logging Configuration
# --------------------------------------------------------------------------------
# Uses basicConfig for the root logger and a named child logger.

import logging

# Root logger configuration
logging.basicConfig(level=logging.DEBUG)

# Create the root logger (no name is provided)
root = logging.getLogger()
root.info('DEBUG message from the root logger')

# Create a child logger (name is provided)
child = logging.getLogger('child')
child.info('INFO message from the child logger')
```

## Logging Config Dict

```python
# Logging Configuration with a Dictionary
# --------------------------------------------------------------------------------
# Uses a dict to define formatters, handlers and loggers.

import logging.config

# Define the logging configuration as a dictionary
config = {

    # Version of the logging configuration
    'version': 1,

    # Define the formatters
    'formatters': {

        # Standard formatter
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        },
    },

    # Define the handlers
    'handlers': {

        # Console handler
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },

    },

    # Root logger configuration
    'root': {
        'handlers': ['console', ],
        'level': 'DEBUG',
    },

    # User logger configuration
    'loggers': {

        # Logger myapp
        'myapp': {
            'handlers': ['console', ],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

# Configure logging using the dictionary-based configuration
logging.config.dictConfig(config)

# Create loggers
root_logger = logging.getLogger()
app_logger = logging.getLogger('myapp')

# Log messages
root_logger.debug('This is a debug message from the root logger')
app_logger.info('This is an info message from the app logger')
```

## Logging Config File

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

## Logging Exceptions

```python
# Logging Exceptions
# --------------------------------------------------------------------------------
# Captures an exception and logs the full stack trace.

import logging

a = 5
b = 0

try:
    c = a / b
except Exception as e:
    logging.error(e, exc_info=True)
    logging.error("Please check the values of a and b")
```

## Logging Formatter

```python
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
```

## Logging Handlers

```python
# Multiple Logging Handlers
# --------------------------------------------------------------------------------
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
```

## Logging Hierarchy

```python
# Logger Hierarchy
# --------------------------------------------------------------------------------
# Shows parent, child and grandchild loggers working together.

import logging

# Basic logging configuration
logging.basicConfig(level=logging.DEBUG)

# Create the root logger (no name is provided)
root = logging.getLogger()
root.setLevel(logging.DEBUG)
root.debug('DEBUG message from the root logger')

# Create a child logger (name is provided)
child = logging.getLogger('child')
child.info('INFO message from the child logger')

# Create a grandchild logger (parent and name are provided)
grandchild = logging.getLogger('child.grandchild')
grandchild.error('CRITICAL message from the grandchild logger')

# Get the logging hierarchy
root.info('Logger hierarchy: {}'.format(root.manager.loggerDict))
```

## Logging Levels

```python
# Logging Levels
# --------------------------------------------------------------------------------
# Demonstrates how to emit messages for each severity level.

import logging

# Basic logging configuration
logging.basicConfig(level=logging.DEBUG)

# Logging levels
logging.debug('Hello world!')
logging.info('Hello world!')
logging.warning('Hello world!')
logging.error('Hello world!')
logging.critical('Hello world!')
```
