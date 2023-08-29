# See chapter 6 for more information about the input() function
var = input('Enter value: ')

# Variable is between 1 and 10 (inclusive)
if 1 <= var <= 10:
    print("Variable is in the positive allowed range")

# Variable is between -10 and -1 (inclusive)
elif -10 <= var <= -1:
    print("Variable is in the negative allowed range")

# Varibale is outside of the allowed range
else:
    print("Condition outside of the allowed range")
