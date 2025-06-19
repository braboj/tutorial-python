# Example: Infinite sequence

def infinite_sequence():
    i = 0
    while True:
        yield i
        i += 1


gen = infinite_sequence()

# The generator is a type of iterator that implements the iterator protocol.

print(next(gen))
print(next(gen))
print(next(gen))

# ... and so on
