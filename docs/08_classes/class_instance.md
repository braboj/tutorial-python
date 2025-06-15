# class_instance

```python
# Class instance with concrete values
# --------------------------------------------------------------------------------
# After defining the Person class, an instance is created with explicit values.
# The object stores these attributes as part of its state. Accessing them later
# confirms that the information persists on the instance.

class Person(object):

    def __init__(self):
        print("Person has ID {}".format(id(self)))


# The person object has a unique id
p1 = Person()
p2 = Person()
```
