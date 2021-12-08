# The ascii() method returns a string containing a printable representation of an object. It escapes the non-ASCII
# characters in the string using \x, \u or \U escapes.

normalText = 'Python is interesting'
print(ascii(normalText))

otherText = 'Pythön is interesting'
print(ascii(otherText))

print('Pyth\xf6n is interesting')
