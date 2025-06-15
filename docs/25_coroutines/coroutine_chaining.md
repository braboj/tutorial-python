# coroutine_chaining

```python
# Example: Coroutine Chaining

def producer(string, next_coroutine):
    tokens = string.split(" ")
    for token in tokens:
        next_coroutine.send(token)
    next_coroutine.close()


def consumer():
    print("I'm the sink, I'll print tokens")
    try:
        while True:
            token = (yield)
            print(token)
    except GeneratorExit:
        print("Done with printing!")


sentence = "Hello, world!"
print(sentence)

# Define token printer (consumer) and activate
printer = consumer()
next(printer)

# Define token splitter (producer)
producer(string=sentence, next_coroutine=printer)

# Output
# ---------------------------
# Hello, world!
# I'm the sink, i'll print tokens
# Hello
# world!
# Done with printing!
```
