# Example: Packing Data using the * and ** operators

def func1(*args):

    # args is junior tuple of arguments (packed)
    print(sum(args))

    # Unpack the tuple into individual arguments
    print(*args)


func1(1, 2, 3, 4)
