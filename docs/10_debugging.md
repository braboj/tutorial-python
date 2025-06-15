# Debugging

## Debug Breakpoints Complex

```python
# Advanced Breakpoint Scenarios
# --------------------------------------------------------------------------------
# This script explores a couple of techniques for stopping execution only when
# certain conditions are met. An if-statement can invoke the builtin breakpoint
# function when values match specific criteria, and you can set a conditional
# breakpoint in pdb with ``break my_script.py:20, x > 10``. Studying these
# patterns helps you focus on the critical moments that reveal bugs.


def process_items(items):
    for item in items:
        if item % 2 == 0:
            breakpoint()  # stops when item is even
        if item > 50:
            import pdb
            pdb.set_trace()  # triggers on large values
        print(f'processed {item}')


if __name__ == "__main__":
    sample = [1, 3, 4, 8, 60, 5]
    process_items(sample)
```

## Debug Pdb

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

## Debug Print

```python
# Debugging with Print Statements
# --------------------------------------------------------------------------------
# This script shows how printing variable values at strategic locations can help
# trace program state. By observing the output, you can identify unexpected
# changes in variables that lead to errors. Adjust the print calls to focus on
# parts of the code you suspect are faulty.


def factorial(n):
    result = 1
    for i in range(1, n):
        result *= i
        print(f'i={i}, result={result}')
    return result


if __name__ == "__main__":
    print(factorial(5))
```
