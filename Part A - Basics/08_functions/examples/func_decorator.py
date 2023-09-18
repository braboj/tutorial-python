def decorator(func):
    def wrapper():
        print('Before function call')
        func()
        print('After function call')
    return wrapper


def welcome():
    print('Welcome to Python')


@decorator
def hello():
    print('Hello world')


# Use the decorator function explicitly
test = decorator(welcome)
test()

# Let Python do the work for us
hello()
