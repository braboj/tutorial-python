from __future__ import annotations
from abc import ABC, abstractmethod


# Interface used by both Leaf and Composite
class IChannel(ABC):

    @abstractmethod
    def configure(self):
        raise NotImplementedError


# Concrete implementation of Leaf
class Channel(IChannel):

    def configure(self):
        return "Channel configured"


# Concrete implementation of Composite
class Device(IChannel):

    def __init__(self):
        self.children = []

    def add(self, c):
        self.children.append(c)
        return self

    def remove(self, c):
        self.children.remove(c)
        return self

    def get_children(self):
        return self.children

    def configure(self):
        # Delegate work to all the children
        for index, child in enumerate(self.children):
            print(f"{index} : {child.configure()}")

        return "Device configured"


if __name__ == "__main__":

    # Define composite product
    product = Device()

    # Add a branch with two leafs
    product.add(
        Device().
            add(Channel()).
            add(Channel())
    )

    # Add a leaf
    product.add(Channel())

    # Execute an operation on the product and its parts
    product.configure()
