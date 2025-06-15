# func_lambda_bytecodes

```python
# Lambda and def produce the same bytecode
# --------------------------------------------------------------------------------
# This script compiles a lambda expression and a regular function to compare
# their bytecode output. Both forms compile into nearly identical instructions.
# Using ``lambda`` therefore carries no extra runtime cost compared to ``def``.

import dis

func1 = lambda x: x * x


def func2(x):
    return x * x


print(dis.dis(func1))
print(dis.dis(func2))
```
