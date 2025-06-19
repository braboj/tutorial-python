# Use the print() function to output text to the console.
# --------------------------------------------------------------------------------
# The print() function is used to output data to the screen. It can take
# multiple arguments and will convert them to strings before printing them.

# By default, print() ends with a newline character.
print("Hello")
print("World")
# Output:
#   Hello
#   World

# You can change this behavior by specifying the end parameter.
print("Hello", end="")
print("World", end="")
# Output:
#   HelloWorld

# A print statement with no arguments prints a newline character.
print("Hello", end="")
print()
print("World", end="")
# Output:
#   Hello
#   World

# You can also specify the separator symbol
print("Hello", "World", sep="")
print("Hello", "World", sep=" ")
print("Hello", "World", sep=", ")
# Output:
#   HelloWorld
#   Hello World
#   Hello, World
