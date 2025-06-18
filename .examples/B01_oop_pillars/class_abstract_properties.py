# Stacking decorators
# --------------------------------------------------------------------------------
# Multiple decorators can be stacked on a single attribute. In this file a
# property is defined using @property together with @abstractmethod. Derived
# classes must supply the concrete implementation for this decorated property.

from abc import ABCMeta, abstractmethod
from six import with_metaclass


class DeviceAbc(with_metaclass(ABCMeta)):
    """Example abstract class

    Usage:

        # Optional
        @property, @staticmethod, @classmethod

        +

        # Obligatory decorator
        @abstractmethod

    Example:

        # Defines and abstract property
        @property
        @abstractmethod
        def prop(self):
            ...

    """

    def __init__(self):
        self._bar = "bar"

    @property
    @abstractmethod
    def bar(self):
        pass

    @abstractmethod
    def foo(self):
        pass


class Samsung(DeviceAbc):

    @property
    def bar(self):
        return self._bar

    def foo(self):
        print('foo')


test = Samsung()
print(test.bar)
test.foo()
