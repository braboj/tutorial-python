# 3_bytestream

```python
import random


def byte_generator(limit=0, header=None):

    # Initialize
    print("Started")
    counter = 0

    # Iterator
    try:
        # Generate bytes from header
        if header:
            while counter < len(header):
                yield header[counter]
                counter += 1

        # Generate random bytes after header
        output = random.randrange(start=0, stop=255, step=1)
        while counter < limit:
            try:
                yield output
                output = random.randrange(start=0, stop=255, step=1)
                counter += 1

            except Exception as e:
                print(e)

    except GeneratorExit:
        print("Terminated")


stream = byte_generator(limit=10, header=[0xDE, 0xAD, 0xBE, 0xEF])

for b in stream:
    print(hex(b))
```
