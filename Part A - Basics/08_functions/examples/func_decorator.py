def decorator(func):
    def wrapper():
        print('Before function call')
        func()
        print('After function call')
    return wrapper


@decorator
def hello():
    print('Hello world')


hello()
