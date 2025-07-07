# Example: String Interning

import sys

# Create two string literals with the same content
str1 = "hello"
str2 = "hello"

# Check if str1 and str2 reference the same object (identity check)
print("> Creating two string literals with the same content")
print("# {} is {}: {}\n".format(str1, str2, str1 is str2))

# Create a non-literal string with the same content
str3 = ""
str3 += "h"
str3 += "e"
str3 += "l"
str3 += "l"
str3 += "o"

# Check if str1 and str2 reference the same object (identity check)
print("> Create a non-literal string with the same content")
print("# {} is {}: {}\n".format(str1, str3, str1 is str3))

# Intern the string referenced by str3
str3 = sys.intern(str3)

# Check if str1 and str3 reference the same object (identity check)
print("> Intern the non-literal string")
print("# {} is {}: {}\n".format(str1, str3, str1 is str3))
