# Example: Logging Objects with hierarchy

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
