# Example: Basic and Advanced Logging Configuration

import logging

# Root logger configuration
logging.basicConfig(level=logging.DEBUG)

# Create the root logger (no name is provided)
root = logging.getLogger()
root.info('DEBUG message from the root logger')

# Create a child logger (name is provided)
child = logging.getLogger('child')
child.info('INFO message from the child logger')
