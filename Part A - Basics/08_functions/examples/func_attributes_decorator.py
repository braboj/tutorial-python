def wrapper(func):
    func.author = "Branimir Georgiev"
    return func


@wrapper
def hello():
    print('Hello world!')


hello()
print(hello.author)
