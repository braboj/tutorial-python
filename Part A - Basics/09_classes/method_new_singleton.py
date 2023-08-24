# Example: Singleton using the __new__ method

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