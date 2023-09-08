import logging

a = 5
b = 0

try:
  c = a / b
except Exception as e:
    logging.error(e, exc_info=True)
    logging.error("Please check the values of a and b")