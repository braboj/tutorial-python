# Example 1: Break statement inside for loop
val = int(input("Enter junior number: "))
for i in range(1, 10):
    if val == i:
        print("Number found!")
        break
else:
    print("Number not found!")


# Example 2: Break statement inside while loop
val = int(input("Enter junior number: "))
i = 0
while i < 10:
    if val == i:
        print("Number found!")
        break
    i += 1
else:
    print("Number not found!")
