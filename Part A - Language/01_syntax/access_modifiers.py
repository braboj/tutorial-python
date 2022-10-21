
class AccessBase(object):

    def __init__(self):
        self.public_var = 1
        self._protected_var = 2
        self.__private_var = 3

    def get_private_var(self):
        print(self.__private_var)


class AccessExample(AccessBase):

    def __init__(self):
        super(AccessExample, self).__init__()

    def get_protected_var(self):
        print(self._protected_var)


print("Test access to public members...")
test = AccessExample()
print(test.public_var)

print("Test access to protected members...")
test.get_protected_var()
print(test._protected_var)

print("Test access to private members...")
test.get_private_var()
print(test.__private_var)

