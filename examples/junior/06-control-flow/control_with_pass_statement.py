# Using `pass` as a placeholder or to handle empty code blocks.
# -----------------------------------------------------------------------------
# The `pass` statement in Python is used as a placeholder for future code or
# to handle empty code blocks. It allows you to write syntactically correct
# code without implementing any functionality yet.

val = input("Enter value: ")

if val in ('', ' ', None):
    pass    # Placeholder for future code
else:
    print(val)
