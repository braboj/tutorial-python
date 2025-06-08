# Example: Different internal representations of the same object

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
