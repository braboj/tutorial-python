# interface_segregation_good

```python
# Interface Segregation Principle - Good Example
# -------------------------------------------------------------------------------
# The Interface Segregation Principle (ISP) breaks large interfaces
# into focused ones. Mixins here provide only the operations each
# device actually needs.

class Device(object):
    # Defines only the common methods for all devices

    def __init__(self, name, *args, **kwargs):
        super(Device, self).__init__(*args, **kwargs)
        self.name = name

    def power_on(self):
        pass

    def power_off(self):
        pass


class SoundMixin(object):
    # Defines only the methods for all sound devices

    def __init__(self, *args, **kwargs):
        super(SoundMixin, self).__init__(*args, **kwargs)

    def volume_up(self):
        pass

    def volume_down(self):
        pass


class VisualMixin(object):
    # Defines only the methods for all visual devices

    def __init__(self, *args, **kwargs):
        super(VisualMixin, self).__init__(*args, **kwargs)

    def brightness_up(self):
        pass

    def brightness_down(self):
        pass


class TypingMixin(object):
    # Defines only the methods for all typing devices

    def __init__(self, *args, **kwargs):
        super(TypingMixin, self).__init__(*args, **kwargs)

    def press(self):
        pass

    def release(self):
        pass

    def hold(self):
        pass


class Keyboard(Device, TypingMixin):
    pass


class HeadSet(Device, SoundMixin):
    pass


class Speaker(Device, SoundMixin):
    pass


class Monitor(Device, VisualMixin):
    pass


class Television(Device, SoundMixin, VisualMixin):
    pass


class Computer(Device, SoundMixin, VisualMixin, TypingMixin):
    pass
```
