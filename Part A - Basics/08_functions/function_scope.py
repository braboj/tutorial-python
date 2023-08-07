# Initialize a variable
var = 1
print(var)


# Define a function that defines a local variable with the same name as the global variable
def myfunction():
    var = 2
    print(var)


# Call the function
myfunction()

# Check that the functiono did not change the value of the global variable
print(var)
