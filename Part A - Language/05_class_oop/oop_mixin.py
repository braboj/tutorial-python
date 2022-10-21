"""
Mixins are an alternative class design pattern that avoids both single-inheritance class fragmentation and
multiple-inheritance diamond dependencies.

https://www.residentmar.io/2019/07/07/python-mixins.html

"""


class Device(object):
    def __init__(self, color, price):
        self.color = color
        self.price = price

    def on(self):
        print("Turn on...")

    def off(self):
        print("Turn off...")


class Camera(object):

    @staticmethod
    def take_picture():
        print("Shoot picture...")

    @staticmethod
    def record_video():
        print("Record video...")


class Keyboard(object):

    @staticmethod
    def press_key():
        print("Press a key...")


class Mouse(object):

    @staticmethod
    def move_mouse():
        print("Move the mouse...")


class Monitor(object):

    @staticmethod
    def display_content():
        print("Display content...")


class TouchScreen(Monitor):

    @staticmethod
    def touch_screen():
        print("Touch the screen...")


class PC(Device, Keyboard, Mouse, Monitor, Camera):
    def __init__(self, color, price):
        super(PC, self).__init__(color, price)
        self.price = price


class Tablet(Device, TouchScreen, Camera):
    def __init__(self, color, price, weight):
        super(Tablet, self).__init__(color, price)
        self.weight = weight


pc = PC(color='black', price=1000)
ipad = Tablet(color='white', price=1000, weight=200)

pc.on()
pc.move_mouse()
pc.display_content()
pc.press_key()
pc.off()

ipad.on()
ipad.touch_screen()
ipad.record_video()
ipad.take_picture()
ipad.display_content()
ipad.off()

