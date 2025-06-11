# Framework: doctest
# --------------------
#
# Demonstrate doctest by verifying simple distance conversions.

# Example: doctest test cases

""" Example: doctest test cases

Run the file with the -v flag to see the results of the tests or use the IDE of your choice
to run the doctest tests.

>>> miles_to_km(1)
1.61
>>> km_to_miles(1)
0.5
"""


def miles_to_km(miles):
    return miles * 1.61


def km_to_miles(km):

    return km / 1.61


