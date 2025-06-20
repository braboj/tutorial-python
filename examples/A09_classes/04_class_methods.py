# Class method used to modify the class itself
# ------------------------------------------------------------------------------
# In Python, class methods can be used to modify the behavior of all instances
# of a class by changing class-level attributes. Class methods are defined
# using the `@classmethod` decorator and take the class itself as the first
# parameter, conventionally named `cls`.

class Male(object):

    NAME_PREFIX = "Mr."

    def __init__(self, name):
        self.name = name

    @classmethod
    def set_prefix(cls, prefix):
        cls.NAME_PREFIX = prefix

    @classmethod
    def get_prefix(cls):
        return cls.NAME_PREFIX

    def show_name(self):
        print(f"{Male.get_prefix()} {self.name}")


john = Male("John")
ivan = Male("Ivan")

# Show the initial name
john.show_name()
ivan.show_name()

# Modify the class-level attribute will affect all instances
Male.set_prefix("Mister")

# Show the modified name
john.show_name()
ivan.show_name()
