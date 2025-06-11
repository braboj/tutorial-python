# Dunder methods for arithmetic operators
# ---------------------------------------------------------------------------
# By defining special arithmetic methods, objects can participate in Python's
# numeric operations. These dunder hooks let a class customize how instances
# respond to +, -, *, and other operators.

class Complex(object):

    def __init__(self, real, imag):
        self.real = float(real)
        self.imag = float(imag)

    def __add__(self, other):
        return Complex(
            real=self.real + other.real,
            imag=self.imag + other.imag
        )

    def __sub__(self, other):
        return Complex(
            real=self.real - other.real,
            imag=self.imag - other.imag
        )

    def __mul__(self, other):
        return Complex(
            real=self.real * other.real,
            imag=self.imag * other.imag
        )

    def __divmod__(self, other):
        return Complex(
            real=self.real % other.real,
            imag=self.imag % other.imag
        )

    def __truediv__(self, other):
        return Complex(
            real=self.real / other.real,
            imag=self.imag / other.imag
        )

    def __floordiv__(self, other):
        return Complex(
            real=self.real // other.real,
            imag=self.imag // other.imag
        )


a = Complex(1, 2)
b = Complex(3, 4)

z = a + b
print(z.real, z.imag)