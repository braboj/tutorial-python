# Function factories to create specialized functions
# --------------------------------------------------------------------------------
# A function factory returns a new function tailored to the argument it
# receives. It enables creation of many small functions without repeating code.
# Each generated function captures the parameters provided to the factory.

def power_of(n):
    def power(x):
        return x ** n

    return power


# Square root
sqrt = power_of(0.5)
print(sqrt(100.0))

# Square
sqr = power_of(2)
print(sqr(10.0))
