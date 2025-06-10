# Calculate the length of a string
# -----------------------------------------------------------------------------
# This code demonstrates how to calculate the symbol length of a string in
# Python. Bear in mind that this is not the same as the byte length of the
# string, which can be different if the string contains  UTF-8 characters that
# are represented by multiple bytes.

text = "0123456789"
print(len(text))
# Output:
# 10

text = 'Здравей!'
print(len(text))
# Output:
# 8
