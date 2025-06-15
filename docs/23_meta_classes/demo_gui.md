# demo_gui

```python
##############################################################################
# Window
#   > Box
#       > Label
##############################################################################


##############################################################################
# Imperative programming
##############################################################################
class Box(object):

    def add(self, what):
        pass


class Label(object):

    def __init__(self, label=""):
        self.label = label

    def add(self):
        pass


class Window(object):
    def __init__(self, title="Window element"):
        self.title = title

        self.box = Box()
        self.add(self.box)
        self.label = Label(label="Hello, label!")
        self.box.add(self.label)

    def add(self, what):
        pass


##############################################################################
# Declarative programming
##############################################################################
class Top(Window):
    title = "Hello, window!"

    class Group(Box):
        class Title(Label):
            label = '"Hello, label!"'


##############################################################################
# Solution???
##############################################################################
```
