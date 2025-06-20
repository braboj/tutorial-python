# Interface Segregation Principle - Bad Example
# ------------------------------------------------------------------------------
# The Interface Segregation Principle (ISP) advises that clients
# should not be forced to depend on methods they do not use.
#
# In this example, we have a base class `Device` that defines methods
# for powering on, powering off, adjusting volume, and brightness. However,
# the `HeadSet` and `Monitor` classes only use a subset of these methods,
# leading to a violation of the ISP.

class Device(object):

    def __init__(self, name):
        self.name = name

    def power_on(self):
        pass

    def power_off(self):
        pass

    def volume_up(self):
        # Code smell: Used only by Headset
        pass

    def volume_down(self):
        # Code smell: Used only by Headset
        pass

    def brightness_up(self):
        # Code smell: Used only by Monitor
        pass

    def brightness_down(self):
        # Code smell: Used only by Monitor
        pass


class HeadSet(Device):

    def __init__(self, name):
        super(HeadSet, self).__init__(name)

    def power_on(self):
        print("Headset powered on")

    def power_off(self):
        print("Headset powered off")

    def volume_up(self):
        print("Headset volume up")

    def volume_down(self):
        print("Headset volume down")


class Monitor(Device):

    def __init__(self, name):
        super(Monitor, self).__init__(name)

    def power_on(self):
        print("Monitor powered on")

    def power_off(self):
        print("Monitor powered off")

    def brightness_up(self):
        print("Monitor brightness up")

    def brightness_down(self):
        print("Monitor brightness down")
