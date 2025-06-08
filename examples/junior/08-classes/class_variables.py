# Example: Class attributes

class Person(object):

    # Class attributes are defined outside of any method and are shared by all instances
    MALE_PREFIX = "Mr."
    FEMALE_PREFIX = "Ms."

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def get_prefix(self):
        """ Demonstrate how to access class attributes from instance methods """

        # The person is male
        if self.sex == "male":
            prefix = self.MALE_PREFIX

        # The person is female
        elif self.sex == "female":
            prefix = self.FEMALE_PREFIX

        # Others
        else:
            prefix = ""

        return prefix

    def get_name(self):
        """ Return the name with the appropriate prefix """
        return "{} {}".format(self.get_prefix(), self.name)


# Create the instances
males = [Person(name="Branimir", sex="male"), Person("Dimitar", sex="male")]

# Class attributes are accessible from the instance methods
print("Default prefix...")
for male in males:
    print(male.get_name())

# Class attributes are accessible from the class itself and junior change will affect all instances
print("Prefix changed...")
Person.MALE_PREFIX = "Sir"
for male in males:
    print(male.get_name())
