# composite

```python
# Example: Composite pattern

from abc import abstractmethod


class IComponent(object):
    # Interface used by both the leaf and composite classes

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def execute(self):
        raise NotImplementedError


class Leaf(IComponent):

    def execute(self):
        return "{} running".format(self.name)


# Concrete implementation of the composite class
class Composite(IComponent):
    # This is the composite class (tree is composed of leafs)

    def __init__(self, name="Root"):
        super(Composite, self).__init__(name)
        self.components = []

    def add(self, c):
        self.components.append(c)
        return self

    def remove(self, c):
        self.components.remove(c)
        return self

    def get_children(self):
        return self.components

    def execute(self):

        # Delegate work to all the children
        for child in self.components:
            print("{} / {}".format(self.name, child.execute()))

        return "{} running".format(self.name)


if __name__ == "__main__":

    # Define composite foo
    product = Composite()
    product.add(Leaf("Leaf 1"))
    product.add(Leaf("Leaf 2"))
    print(product.execute())

    print()

    # Nested composite foo
    product.add(
        Composite("Subsystem A")
        .add(Leaf("Leaf 1"))
        .add(Leaf("Leaf 2"))
    )
    print(product.execute())
```
