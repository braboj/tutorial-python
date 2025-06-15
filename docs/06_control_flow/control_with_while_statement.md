# control_with_while_statement

```python
# Repeating code with `while` loops until a condition is met.
# --------------------------------------------------------------------------------
# Loops that use the `while` statement to repeat a block of code as long as a
# condition is true. This is useful when the number of iterations is not known
# beforehand, and the loop continues until a specific condition is met.

while True:
    cmd = input("Enter a command (or 'exit' to quit): ")
    if cmd.lower() == 'exit':
        print("Exiting the loop.")
        break
    else:
        print(f"You entered: {cmd}")
```
