import time

# per_counter, perf_counter_ns
c1 = time.perf_counter()
time.sleep(1)
c2 = time.perf_counter()
print(c1, c2, c2 - c1)