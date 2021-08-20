def coroutine():
    print("Coroutine has been started!")
    output = "foo"
    while True:
        text = yield output
        print("Coroutine received :", text)
        output = text[::-1] if text else "boo"


cr = coroutine()

print("Coroutine sent : {0}".format(next(cr)))          # 1. Activate the coroutine
print("Coroutine sent : {0}".format(next(cr)))          # 2. First call to the coroutine to get data
print("Coroutine sent : {0}".format(cr.send("abc")))    # 3. Second call to the coroutine to send data
