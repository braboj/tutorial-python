"""
for else loop

Else is called only when there were no calls to break in the loop
1. Eliminate flag set in for to show that an element was found
2. Handle exceptions in a pythonic way

for, else, continue, break

"""

# USECASE 01
test = [1, 2, 3, 4, 5]
num = 6
for x in test:
    if x == num:
        print("Element found")
        break
else:
    print("Element not found")


# USECASE 02
test = [1, 2, 0]
num = 1

for x in test:
    try:
        num / x
    except ZeroDivisionError:
        break

else:
    print("All denominators passed")