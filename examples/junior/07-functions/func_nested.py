def absolute_value(x):
    # Emulate the built-in abs() function, e.g. abs(-1) == 1 and abs(1) == 1

    def negative_value():
        # An inner function can access the variables of the outer function

        return -x

    def positive_value():
        # An inner function can also access the variables of the outer function

        return x

    # Use the inner functions to return the correct value
    return negative_value() if x < 0 else positive_value()


print(absolute_value(-1))  # 1
print(absolute_value(1))   # 1
