# Example: Singleton Pattern with __new__


class Singleton(object):

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)

        return cls.__instance


s1 = Singleton()
s2 = Singleton()

print(s1 is s2)

