# Exiting loops prematurely with the `break` statement.
# -----------------------------------------------------------------------------
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
