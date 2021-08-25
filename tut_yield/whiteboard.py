def producer(string, next_coroutine):
    tokens = string.split(" ")
    for token in tokens:
        next_coroutine.send(token)
    next_coroutine.close()


def consumer():
    print("I'm sink, i'll print tokens")
    try:
        while True:
            token = (yield)
            print(token)
    except GeneratorExit:
        print("Done with printing!")


sentence = "Hello world!"
print(sentence)

# Define token printer (sink) and activate
printer = consumer()
next(printer)

# Define token splitter (producer)
producer(string=sentence, next_coroutine=printer)


# # Implementation with a colllection
# def evens_A(stream):
#     them = []
#     for n in stream:
#         if n % 2 == 0:
#             them.append(n)
#     return them
#
#
# # Implementaton with a generator
# def evens_B(stream):
#     for n in stream:
#         if n % 2 == 0:
#             yield n
#
#
# num = [x for x in range(10)]
#
# print("-" * 80)
# for x in evens_A(num):
#     print(x)
#
# print("-" * 80)
# for x in evens_B(num):
#     print(x)