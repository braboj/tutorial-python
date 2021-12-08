"""
Scenario : At Hilscher the test framework uses meta-classes to scan for devices with open channels. If 2 or more
device classes are found, then the network creates a new class with all device classes as base classes. This leads
to a problem as the order the device classes are found is not always guaranteed.

Solution: Use custom device class to ensure the right methods are used for the respective device

"""


class ReloadMeta(type):

    registry = {}

    def __new__(mcs, class_name, bases, namespace):

        module_name = namespace['__module__']

        try:
            current = mcs.registry[module_name][class_name]
        except KeyError:
            current = None
        if current:
            mcs.regenerate(current, namespace)
            return current

        cls = type.__new__(mcs, class_name, bases, namespace)
        mcs.registry.setdefault(module_name, {})[class_name] = cls

        return cls

    def regenerate(cls, namespace):

        print("Reloading class %s" % cls)

        for name in list(cls.__dict__.keys()):
            if name in ['__name__', '__metaclass__',
                        '__module__', '__dict__',
                        '__weakref__', '__bases__']:
                continue
            delattr(cls, name)

        for name, value in namespace.items():
            setattr(cls, name, value)

        return cls


if __name__ == '__main__':

    # First class with method test
    class C(object, metaclass=ReloadMeta):

        def test(self):
            print('first {0}'.format(self))


    c = C()
    c.test()

    # Second class with new method test
    class C(object, metaclass=ReloadMeta):

        def test(self):
            print('second {0}'.format(self))


    c.test()
