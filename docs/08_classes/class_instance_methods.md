# class_instance_methods

```python
# Class instance with instance methods
# --------------------------------------------------------------------------------
# Instance methods operate on a particular object and have access to its state.
# They typically receive the instance as the first parameter. Calling these
# methods affects only the object that invoked them.

class Person(object):

    def do_something(self):
        print("{} is doing something".format(self))

    def do_something_with(self, something, someone):
        print("{} is doing {} with {}".format(self, something, someone))


# Create the instance
p = Person()
p.do_something()
p.do_something_with("nothing", "no one")
```
