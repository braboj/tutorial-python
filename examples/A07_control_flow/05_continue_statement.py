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
