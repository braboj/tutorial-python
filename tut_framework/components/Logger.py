import logging

getLogger = logging.getLogger()

# Define framework logging format
LOG_LEVEL = logging.INFO
fmt = "[%(asctime)s:%(msecs)s : %(levelname)s : %(name)-20s] : %(message)s"
logging.basicConfig(format=fmt, level=LOG_LEVEL, datefmt="%H:%M:%S")


