import tut_time.datetime
import logging

logging.basicConfig(level=logging.INFO)

now = tut_time.datetime.datetime.now()
logging.info(now)

yesterday = now.replace(day=now.day - 1)
logging.info(yesterday)

future_day = tut_time.datetime.datetime(year=2022, month=1, day=17)
logging.info(future_day)

time_remaining = future_day - now
logging.info(time_remaining)

tzinfo = now.tzname()
logging.info(tzinfo)