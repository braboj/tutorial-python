# debug_pdb

```python
# Interactive Debugging with pdb
# --------------------------------------------------------------------------------
# The pdb module offers an interactive environment for stepping through code.
# Breakpoints allow you to pause execution and inspect variables at each stage.
# Use commands like `n`, `s`, and `c` to move around while troubleshooting.


def add_numbers(numbers):
    total = 0
    for value in numbers:
        breakpoint()
        total += value
    return total


if __name__ == "__main__":
    print(add_numbers([1, 2, 3]))
```
