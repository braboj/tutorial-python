# class_named_constructor_representation

```python
# Different internal representations of the same object
# --------------------------------------------------------------------------------
# A class may provide alternate constructors that store data in various formats.
# Each representation exposes the same behavior to callers. Selecting one or
# another depends on the needs of the application.

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_json(cls, data):
        return cls(**data)

    @staticmethod
    def from_csv(data):
        name = data[0]
        age = data[1]
        return Person(name=name, age=age)


# Mock data
json_data = {'name': 'mayank', 'age': 27}
csv_data = [('mayank', 27), ]

person = Person.from_json(json_data)
print(person.name, person.age)

person = Person.from_csv(csv_data[0])
print(person.name, person.age)
```
