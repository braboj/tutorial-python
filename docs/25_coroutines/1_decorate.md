# 1_decorate

```python
def prime(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr

    return start


def source(text, target):
    tokens = text.split(" ")
    for token in tokens:
        target.send(token)
    target.close()


@prime
def pattern_filter(pattern="ing", target=None):
    print("Searching for {}".format(pattern))
    try:
        while True:
            token = (yield)
            if pattern in token:
                target.send(token)
    except GeneratorExit:
        print("Done with filtering!!")


@prime
def sink():
    print("I'm sink, i'll print tokens")
    try:
        while True:
            token = (yield)
            print(token)
    except GeneratorExit:
        print("Done with printing!")


sentence = "Bob is running behind junior fast moving car"
source(text=sentence,
       target=pattern_filter(
             target=sink()
         )
       )
```
