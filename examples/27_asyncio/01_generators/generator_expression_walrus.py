# Example: Walrus operator in a generator expression

# The walrus operator (:=) assigns values to variables as part of a larger
# expression. It is also known as the assignment expression and is supported
# in Python 3.8 and above. It is useful for troubleshooting, dictionary creation,
# and more.

gen = (x for x in range(10) if (y := x % 2) == 1)
for x in gen:
    print(x, y)
