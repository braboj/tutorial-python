# Access modifiers and name mangling
# -----------------------------------------------------------------------------
#
# Public attributes have no leading underscores and can be accessed from
# anywhere.  A single leading underscore marks an attribute as "protected" by
# convention, signalling it should only be used by the class and its
# subclasses.  A double underscore triggers name mangling which makes the
# attribute effectively private to the class.  This prevents accidental
# access from subclasses or external code.

class AccessModifiers(object):

    def __init__(self):

        # Public: Accessible from anywhere
        self.public = "public"

        # Protected: Accessible from the class and subclasses
        self._protected = "protected"

        # Private attribute -- the name will be mangled to _AccessModifiers__private
        # and is intended for use only inside this class
        self.__private = "private"


class AccessModifiersChild(AccessModifiers):

    def __init__(self):
        super(AccessModifiersChild, self).__init__()

        # Public: Accessible from anywhere
        print(self.public)

        # Protected: Accessible from the class and subclasses
        print(self._protected)

        # Private: name is mangled so direct access fails in the child class
        try:
            print(self.__private)

        except AttributeError as e:
            print(e)


test = AccessModifiersChild()
