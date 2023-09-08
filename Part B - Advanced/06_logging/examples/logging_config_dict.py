# Example: Logging Configuration with a Dictionary

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
