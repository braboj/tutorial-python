def producer(string, next_coroutine):
    tokens = string.split(" ")
    for token in tokens:
        next_coroutine.send(token)
    next_coroutine.close()


def pattern_filter(pattern="ing", next_coroutine=None):
    print("Searching for {}".format(pattern))
    try:
        while True:
            token = (yield)
            if pattern in token:
                next_coroutine.send(token)
    except GeneratorExit:
        print("Done with filtering!!")


def consumer():
    print("I'm sink, i'll print tokens")
    try:
        while True:
            token = (yield)
            print(token)
    except GeneratorExit:
        print("Done with printing!")


# Define token printer (sink) and activate
printer = consumer()
next(printer)

# Define token filterer (middle) and activate
filterer = pattern_filter(next_coroutine=printer)
next(filterer)

# Define token splitter (producer)
sentence = "Bob is running behind a fast moving car"
producer(string=sentence, next_coroutine=filterer)
