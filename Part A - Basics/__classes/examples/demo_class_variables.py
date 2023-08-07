class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("{0} eating ...".format(self.name))

    def sleep(self):
        print("{0} sleeping ...".format(self.name))


class Doctor(Person):

    oath = "I swear to fulfill, to the best of my ability and judgment."

    def operate(self, patient):
        print("{0} operating on {1} ...".format(self.name, patient))


# Create doctor instances
doctor_A = Doctor(name="Branimir Georgiev", age=40)
doctor_B = Doctor(name="Dimitar Ivanov", age=50)

# Check if oath is the same to all doctor instances
print(doctor_A.oath)
print(doctor_B.oath)
print(doctor_A.oath == doctor_B.oath)

# Change the oath
Doctor.oath = "I swear to fulfill, to the best of my ability and judgment, this covenant: I will" \
              "respect the hard-won scientific gains of those physicians in whose steps " \
              "I walk, and gladly share such knowledge as is mine with those who are to follow."

# Check if the oath is the same to all doctor instances
print(doctor_A.oath)
print(doctor_B.oath)
print(doctor_A.oath == doctor_B.oath)


# Now try to change the oath using an instance. In this particular case Python will create
# dynamically a new instance attribute `oath`.
doctor_A.oath = "I swear to fulfill, to the best of my ability and judgment."

# Check if the oath is the same to all doctor instances
print(doctor_A.oath)
print(doctor_B.oath)
print(doctor_A.oath == doctor_B.oath)
