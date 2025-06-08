numbers = [1, 2, 3, 4, 5, 6]

# Print all odd numbers in the list until 5
for num in numbers:
    if num % 2 == 0:
        continue
    elif num == 5:
        break
    else:
        print(num)