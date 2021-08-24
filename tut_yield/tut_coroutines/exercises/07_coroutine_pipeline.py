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


def print_token():
    print("I'm sink, i'll print tokens")
    try:
        while True:
            token = (yield)
            print(token)
    except GeneratorExit:
        print("Done with printing!")


# Define token printer (sink)
pt = print_token()
next(pt)

# # Define token filterer (middle)
pf = pattern_filter(next_coroutine=pt)
next(pf)

# # Define token splitter (producer)
sentence = "Bob is running behind a fast moving car"
producer(string=sentence, next_coroutine=pf)
