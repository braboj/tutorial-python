# Mixin class
# --------------------------------------------------------------------------------
# Demonstrates mixin class.

class RemoteMixin(object):

    def __init__(self, brand=None, volume=0, *args, **kwargs):

        # This syntax is required in order to guarantee that the MRO is not broken
        super(RemoteMixin, self).__init__(*args, **kwargs)

        # Mixin specific attributes
        self.brand = brand
        self.volume = volume

    def volume_up(self):
        self.volume += 1

    def volume_down(self):
        self.volume -= 1

    def status(self):
        print("Brand: {}".format(self.brand))
        print("Volume: {}".format(self.volume))


class JvcRemote(RemoteMixin, object):
    """ Mixins should be always inherited first """

    def __init__(self):
        super(JvcRemote, self).__init__(brand="JVC", volume=10)

    def status(self):
        super(JvcRemote, self).status()

    @staticmethod
    def learn():
        print("Learn button")


class SonyRemote(RemoteMixin, object):
    """ Mixins should be always inherited first """

    def __init__(self):
        super(SonyRemote, self).__init__(brand="Sony", volume=5)

    @staticmethod
    def home():
        print("Home button")


remote = JvcRemote()
actions = ["volume_up", "status", "volume_down", "status", "learn", "status"]
for action in actions:
    print("Action: {}".format(action))
    func = getattr(remote, action)
    func()

print("\n")

remote = SonyRemote()
actions = ["volume_up", "status", "volume_down", "status", "home", "status"]
for action in actions:
    print("Action: {}".format(action))
    func = getattr(remote, action)
    func()
