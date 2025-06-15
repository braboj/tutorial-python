# facade

```python
# Example: Facade Pattern

class PumpSystem(object):

    @staticmethod
    def prepare():
        print("SubsystemA prepare ...")

    @staticmethod
    def run():
        print("SubsystemA run ...")


class VentilationSystem(object):

    @staticmethod
    def prepare():
        print("SubsystemB prepare ...")

    @staticmethod
    def run():
        print("SubsystemB run ...")


class ComplexSystemFacade(object):

    def __init__(self):
        self._subsystemA = PumpSystem()
        self._subsystemB = VentilationSystem()

    def run(self):
        self._subsystemA.prepare()
        self._subsystemB.prepare()
        self._subsystemA.run()
        self._subsystemB.run()


def main():
    system = ComplexSystemFacade()
    system.run()


if __name__ == "__main__":
    main()
```
