import tut_time.datetime
import time
import logging

logging.basicConfig(level=logging.INFO)

today = tut_time.datetime.date.today()
logging.info(today)

timestamp = time.time()
today.fromtimestamp(timestamp)
logging.info(today)

logging.info((today.year, today.month, today.day, ))

today = today.replace(year=today.year + 1)
logging.info((today.year, today.month, today.day, ))