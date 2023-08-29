# Example: Class attributes

class Person(object):

    # Class attributes are defined outside of any method and are shared by all instances
    male_prefix = "Mr."
    female_prefix = "Ms."

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def get_prefix(self):
        """ Demostrate how to access class attributes from instance methods """

        # The person is male
        if self.sex == "male":
            prefix = self.male_prefix

        # The person is female
        elif self.sex == "female":
            prefix = self.female_prefix

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

# Class attributes are accessible from the class itself and a change will affect all instances
print("Prefix changed...")
Person.male_prefix = "Sir"
for male in males:
    print(male.get_name())