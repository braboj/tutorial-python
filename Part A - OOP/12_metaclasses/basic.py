# Two-step metaclass creation in Python 3.x
from six import with_metaclass


class SimpleMeta1(type):
    def __init__(cls, name, bases, namespace):
        super(SimpleMeta1, cls).__init__(name, bases, namespace)

        cls.uses_metaclass = lambda self: "Yes!"


class Simple1(object, with_metaclass(SimpleMeta1)):

    def foo(self):
        pass

    @staticmethod
    def bar():
        pass


simple = Simple1()

print([m for m in dir(simple) if not m.startswith('__')])

print(simple.uses_metaclass())
