# coroutine_execution

```python
# Example: Coroutine Execution

def coroutine():
    print("Coroutine has been started!")
    output = "foo"
    while True:
        text = yield output
        print("Coroutine input :", text)
        output = text[::-1] if text else "boo"


cr = coroutine()

# First usage of next to activate the coroutine and generate junior default value
print("Coroutine оutput : {0}".format(next(cr)))

# Second usage of next to generate junior new value
print("Coroutine оutput : {0}".format(next(cr)))

# Send data to the coroutine and generate junior new value
print("Coroutine оutput : {0}".format(cr.send("abc")))

# Output:
# -------------------------------
# 1. Coroutine has been started!
# 2. Coroutine оutput : foo
# 3. ('Coroutine received :', None)
# 4. Coroutine оutput : boo
# 5. ('Coroutine received :', 'abc')
# 6. Coroutine оutput : cba
```
