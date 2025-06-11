# Dunder methods for attribute access
# ---------------------------------------------------------------------------
# Attribute related dunder methods such as __getattr__, __setattr__ and
# __delattr__ give objects dynamic control over attribute access. They enable
# customized lookup, assignment and deletion behavior.

class Complex(object):

    def __init__(self, real, imag):
        self.real = float(real)
        self.imag = float(imag)

    def __setattr__(self, key, value):
        print("Setting attribute: {} = {}".format(key, value))

    def __delattr__(self, item):
        print("Deleting attribute: {}".format(item))

    def __getattr__(self, item):
        print("Getting attribute: {}".format(item))
        return item

z = Complex(1, 2)
setattr(z, "real", 3)
delattr(z, "real")
print(getattr(z, "real"))
