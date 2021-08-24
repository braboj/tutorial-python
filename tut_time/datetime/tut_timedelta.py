import tut_time.datetime
import logging

logging.basicConfig(level=logging.INFO)

# Basic operations
t1 = tut_time.datetime.datetime(year=2020, month=5, day=17, hour=16, minute=0, second=00, microsecond=0)
t2 = tut_time.datetime.datetime(year=2021, month=5, day=17, hour=16, minute=30, second=1, microsecond=500000)
delta = t2 - t1
logging.info((type(delta)))
logging.info(delta)
logging.info((delta.days, delta.seconds, delta.microseconds))
logging.info(delta.total_seconds())

# Save start time
t1 = tut_time.datetime.datetime.now()
logging.basicConfig(level=logging.INFO)
logging.info(t1)

# Perform an operation
counter = 0
while True:
    counter += 1
    if counter > 20000000:
        break

# Save end time
t2 = tut_time.datetime.datetime.now()
logging.info(t2)

# Calculate timestamp difference using datetime
delta = t2 - t1
logging.info(delta)
logging.info((delta.seconds, delta.microseconds))
logging.info(delta.seconds + delta.microseconds / 1000000.0)
logging.info(delta.total_seconds() * 1000000)

if __name__ == "__main__":
    pass
