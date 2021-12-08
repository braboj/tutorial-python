##############################################################################
# EXAMPLE 1 : Register leaf classes and count them
##############################################################################

# 1. Metaclass definition
class RegisterLeafClasses(type):
    def __init__(cls, name, bases, namespace):
        super(RegisterLeafClasses, cls).__init__(name, bases, namespace)

        if not hasattr(cls, 'registry'):
            cls.registry = set()

        cls.registry.add(cls)
        cls.registry -= set(bases)  # Remove base classes

    # Class property
    @property
    def count(cls):
        return len(cls.registry)

    # Metamethods, called on class objects:
    def __iter__(cls):
        return iter(cls.registry)

    def __str__(cls):
        if cls in cls.registry:
            return cls.__name__
        return cls.__name__ + ": " + ", ".join([sc.__name__ for sc in cls])


# 2. Custom root class
class Color(object, metaclass=RegisterLeafClasses):
    pass


# 3. Derived classes
class Blue(Color): pass
class Red(Color): pass
class Green(Color): pass
class Yellow(Color): pass
print(Color)

# 4. Tests
class PhthaloBlue(Blue): pass
class CeruleanBlue(Blue): pass
print(Color)

for c in Color: # Iterate over subclasses
    print(c)

print(Color.count)


##############################################################################
# EXAMPLE 2 : Example from Hilscher Framework
##############################################################################
class Registrar(type):

    """ A meta class used to generate a list of all subclasses of a class """
    def __init__(cls, name, bases, dct):
        super(Registrar, cls).__init__(name, bases, dct)
        cls.register(cls)

    @classmethod
    def list(mcs):
        for attrib in getattr(mcs, 'classes', tuple()):
            yield attrib

    # Metamethod used to register classes
    @classmethod
    def register(mcs, cls):

        try:
            # Create reference to classes attribute
            classes = mcs.classes

        except AttributeError:
            # Create classes attribute and create reference
            classes = mcs.classes = []
            mcs.count = 0

        # Use reference to populate registry
        classes.append(cls)


class ClassToRegister1(object, metaclass=Registrar): pass
class ClassToRegister2(ClassToRegister1): pass

a = ClassToRegister1()
b = ClassToRegister2()

for x in Registrar.list():
    print(x)



