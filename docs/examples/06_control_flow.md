# Control Flow

## Control With Break Statement

```python
# Exiting loops prematurely with the `break` statement.
# --------------------------------------------------------------------------------
# The `break` statement is used to exit a loop prematurely. It can be used in
# both `for` and `while` loops. When the `break` statement is encountered,
# the loop is terminated immediately, and control is transferred to the next
# statement following the loop.

# Break statement inside for loop
val = int(input("Guess a number: "))
for i in range(1, 10):
    if val == i:
        print("You guessed the number!")
        break
else:
    print("You did not guess the number!")


# Break statement inside while loop
val = int(input("Guess a new number: "))
i = 0
while i < 10:
    if val == i:
        print("You guessed the number!")
        break
    i += 1
else:
    print("You did not guess the number!")
```

## Control With Continue Statement

```python
# Skipping iterations in loops with the `continue` statement.
# --------------------------------------------------------------------------------
# When the `continue` statement is encountered, the rest of the code
# in the current iteration is skipped, and control is transferred to the next
# iteration of the loop.

numbers = [1, 2, 3, 4, 5, 6]

# Print numbers, skipping even numbers and breaking on 5
for num in numbers:
    if num % 2 == 0:
        continue
    elif num == 5:
        break
    else:
        print(num)
```

## Control With For Statement

```python
# Iterating over sequences using `for` loops.
# --------------------------------------------------------------------------------
# Loops that use the `for` statement to iterate over a sequence or other
# iterable objects are useful for executing a block of code a fixed number of
# times (we know the number of iterations in advance).

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

## Control With If Statement

```python
# Conditional logic using `if`, `elif`, and `else` to handle different cases based on conditions.
# --------------------------------------------------------------------------------
# The conditional statements in Python allow you to control the flow of your
# program based on certain conditions. This way we can execute different
# blocks of code depending on the condition that is met.
#
# Bear in mind that if a condition is met, the code block will be executed and
# the rest of the code blocks will be skipped. If no condition is met, the
# code block in the `else` statement will be executed, if it exists.

var = int(input('Enter value: '))

if 1 <= var <= 10:
    print("Variable is a valid positive number")

elif -10 <= var <= -1:
    print("Variable is a valid negative number")

else:
    print("Variable is not a valid positive or negative number")
```

## Control With Pass Statement

```python
# Using `pass` as a placeholder or to handle empty code blocks.
# --------------------------------------------------------------------------------
# The `pass` statement in Python is used as a placeholder for future code or
# to handle empty code blocks. It allows you to write syntactically correct
# code without implementing any functionality yet.

val = input("Enter value: ")

if val in ('', ' ', None):
    pass    # Placeholder for future code
else:
    print(val)
```

## Control With While Statement

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
