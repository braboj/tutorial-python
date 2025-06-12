# Singleton using the __new__ method
# --------------------------------------------------------------------------------
# By overriding __new__, this class ensures that only one instance ever exists.
# The method stores the created object and returns it on subsequent calls.
# Such control over object creation implements the singleton pattern.

class Singleton(object):

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            print("Creating singleton...")
            cls.__instance = object.__new__(cls)

        else:
            print("Singleton already exists...")

        return cls.__instance


s1 = Singleton()
s2 = Singleton()
print(s1 == s2)
print(s1 is s2)
