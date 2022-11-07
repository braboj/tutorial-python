class Doctor(object):
    oath = "I swear to fulfill, to the best of my ability and judgment."

    @classmethod
    def get_oath(cls):
        print(cls.oath)


# Use a class method to print the oath
Doctor.get_oath()

# Use a class object to print the oath
doc = Doctor()
doc.get_oath()