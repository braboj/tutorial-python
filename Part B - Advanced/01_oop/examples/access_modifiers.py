# Example: Access modifiers

class AccessModifiers(object):

    def __init__(self):

        # Public: Accessible from anywhere
        self.public = "public"

        # Protected: Accessible from the class and subclasses
        self._protected = "protected"

        # Private: Accessible only from the class
        self.__private = "private"


class AccessModifiersChild(AccessModifiers):

    def __init__(self):
        super(AccessModifiersChild, self).__init__()

        # Public: Accessible from anywhere
        print(self.public)

        # Protected: Accessible from the class and subclasses
        print(self._protected)

        # Private: Not accessible from the class
        try:
            print(self.__private)

        except AttributeError as e:
            print(e)


test = AccessModifiersChild()
