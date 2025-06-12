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
