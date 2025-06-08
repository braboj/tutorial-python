# Example: Function as a decorator for a class

def counter(start_value=1):
    # This is the decorator function with the required interface

    def decorator(cls):
        # This is the decorator function with the class as parameter

        # Add the attribute to the class
        setattr(cls, 'counter', start_value)

        # Return the class
        return cls

    return decorator


# Apply the class decorator with attribute
@counter(start_value=1)
class BaseClass(object):
    pass


# Use the explicit syntax
DecoratedClass = counter(start_value=1)(BaseClass)
obj = DecoratedClass()
print(obj.counter)  # Output: 1

# Let Python do the work for us
decorated_class = BaseClass()
print(decorated_class.counter)  # Output: 1
