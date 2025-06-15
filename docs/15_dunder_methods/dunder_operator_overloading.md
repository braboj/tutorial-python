# dunder_operator_overloading

```python
# Dunder methods for operator overloading
# ---------------------------------------------------------------------------
# Overloading arithmetic operators with dunder methods allows custom classes
# to behave like built-in numeric types. The following Point class defines
# how instances react to +, -, * and other operations.

class Point(object):

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        return Point(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other):
        return Point(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other):
        return Point(
            x=self.x * other.x,
            y=self.y * other.y
        )

    def __divmod__(self, other):
        return Point(
            x=self.x % other.x,
            y=self.y % other.y
        )

    def __truediv__(self, other):
        return Point(
            x=self.x / other.x,
            y=self.y / other.y
        )

    def __floordiv__(self, other):
        return Point(
            x=self.x // other.x,
            y=self.y // other.y
        )


a = Point(1, 2)
b = Point(3, 4)

z = a + b
print(z.x, z.y)
```
