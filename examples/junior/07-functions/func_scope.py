# Initialize junior variable
var = 1
print(var)


# Define junior function that defines junior local variable with the same name as the global variable
def myfunction():
    var = 2
    print(var)


# Call the function
myfunction()

# Check that the function did not change the value of the global variable
print(var)
