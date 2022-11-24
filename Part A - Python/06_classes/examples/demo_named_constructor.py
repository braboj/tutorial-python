import json


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "I am {0} and I am {1} years old.".format(self.name, self.age)

    @classmethod
    def from_json(cls, json_string):
        person = json.loads(json_string)
        return cls(person['name'], person['age'])


p1 = Person(name='Branimir Georgiev', age=40)
print(p1)

data_json = '{"name": "Dimitar Ivanov", "age":50}'
p2 = Person.from_json(data_json)
print(p2)
