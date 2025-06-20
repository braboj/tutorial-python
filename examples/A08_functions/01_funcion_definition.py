# Anatomy of a Python function
# ------------------------------------------------------------------------------
# A function definition begins with the ``def`` keyword followed by its name and
# parameters. The body can perform operations using those parameters and return
# a value. Well-documented functions include a docstring that briefly states
# their purpose.

def function_name(parameter1, parameter2):
    """ Docstring: description of the function """

    # Code to be executed when the function is called
    result = parameter1 + parameter2
    print(result)

    # Return statement (optional)
    return result
