def simple_coroutine():
    print("coroutine has been started!")
    output = "foo"
    while True:
        text = yield output
        print("coroutine received: ", text)
        output = text


cr = simple_coroutine()
print(cr)
print(cr.next())
print(cr.send("abc"))