# debug_print

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
