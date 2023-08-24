import pprint


class DemoClass(object):

    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = {
            "a": [1, 2],
            "b": [3, 4]
        }


demo = DemoClass()
pprint.pprint(vars(demo), indent=5, width=80)