# Example: Basic and Advanced Logging Configuration

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



