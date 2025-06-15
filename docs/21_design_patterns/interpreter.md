# interpreter

```python
# Example: Interpreter Pattern

# Abstract Expression
class Expression(object):

    def interpret(self, context):
        raise NotImplementedError


# Terminal Expression
class Number(Expression):

    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value


# Non-terminal Expression
class Add(Expression):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)


# Context
class Context(object):

    def __init__(self):
        self.variables = {}

    def set(self, variable, value):
        self.variables[variable] = value

    def get(self, variable):
        return self.variables.get(variable, 0)


# Client code
if __name__ == "__main__":

    context = Context()
    context.set("x", 10)
    context.set("y", 5)

    expression = Add(
        Number(context.get("x")),
        Number(context.get("y"))
    )

    result = expression.interpret(context)
    print("Result: {}".format(result))
```
