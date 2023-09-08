def average(start_value=0):
    avg = float(start_value)
    counter = 1
    while True:
        new_value = yield avg
        avg = avg + (new_value - avg) / counter
        counter += 1


test_avg = average(start_value=0)
next(test_avg)

assert(test_avg.send(1) == 1)
assert(test_avg.send(2) == 1.5)
assert(test_avg.send(3) == 2)
assert(test_avg.send(4) == 2.5)
assert(test_avg.send(4) == 2.8)
assert(test_avg.send(4) == 3)

