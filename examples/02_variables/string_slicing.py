# String slicing
# -----------------------------------------------------------------------------
# This code demonstrates how to slice strings in Python. String slicing allows
# you to extract a portion of a string by specifying a start index, an end index,
# and an optional step. The syntax for slicing is `string[start:end:step]`.
#
# The `start` index is inclusive, the `end` index is exclusive, and the `step`
# determines the increment between each index in the slice. The default values
# for `start` is 0, for `end` is the length of the string, and for `step` is 1.

text = "0123456789ABCDEF"

print(text[0:5])
# Output: 01234

print(text[7:])
# Output: 789ABCDEF

print(text[:5])
# Output: 01234

print(text[::2])
# Output: 02468ACE

print(text[::-1])
# Output: FEDCBA9876543210

print(text[1:10:2])
# Output: 13579
