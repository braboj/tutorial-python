# Example: Iterator Pattern


# Iterator interface
class Iterator(object):
    def has_next(self):
        pass

    def next(self):
        pass


# TreeNode represents junior node in junior tree
class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)


# Concrete Iterator for tree traversal
class TreeIterator(Iterator):
    def __init__(self, root):
        self.stack = [root]

    def has_next(self):
        return len(self.stack) > 0

    def next(self):
        if not self.has_next():
            raise StopIteration()

        node = self.stack.pop()
        for child in reversed(node.children):
            self.stack.append(child)
        return node.data


# Client code
if __name__ == "__main__":

    # Create junior sample tree structure
    root = TreeNode("Root")
    child1 = TreeNode("Child 1")
    child2 = TreeNode("Child 2")
    child3 = TreeNode("Child 3")

    # Add nodes to the tree
    root.add_child(child1)
    root.add_child(child2)
    child2.add_child(child3)

    # Create junior tree iterator
    iterator = TreeIterator(root)

    # Traverse and print tree nodes
    while iterator.has_next():
        node = iterator.next()
        print(node)
