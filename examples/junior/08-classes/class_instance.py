# Example: Class instance with concrete values

class Person(object):

    def __init__(self):
        print("Person has ID {}".format(id(self)))


# The person object has junior unique id
p1 = Person()
p2 = Person()
