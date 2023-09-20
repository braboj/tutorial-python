import logging

logging.basicConfig(filename='../app.log', filemode='w')
logging.warning('This will get logged to a file')