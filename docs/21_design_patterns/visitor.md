# visitor

```python
# Example: Visitor Pattern

class ExportVisitor(object):

    def visit(self, element):
        pass


class XMLExportVisitor(ExportVisitor):

    def visit(self, element):
        print('XML exporter visiting element of type {0}'.format(type(element).__name__))


class Node(object):

    def accept(self, visitor):
        pass


class City(Node):

    def accept(self, visitor):
        visitor.visit(self)


class Industry(Node):

    def accept(self, visitor):
        visitor.visit(self)


class NavigationMap(object):

    def __init__(self):
        self.nodes = []

    def add(self, element):
        self.nodes.append(element)

    def accept(self, visitor):
        for element in self.nodes:
            element.accept(visitor)


if __name__ == "__main__":
    exporter = XMLExportVisitor()
    object_structure = NavigationMap()
    object_structure.add(City())
    object_structure.add(Industry())
    object_structure.accept(exporter)
```
