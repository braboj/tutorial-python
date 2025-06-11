# Framework: unittest
# ----------------------
#
# Validate App conversion functions and type checking using
# unittest.TestCase.

# Example: unittest test case

import unittest
import logging
from ..examples.app import App

# Setup the logging
logging.basicConfig(level=logging.DEBUG)


class Test(unittest.TestCase):

    def setUp(self):
        self.app = App()

    def test_miles_to_km(self):
        self.assertEqual(self.app.miles_to_km(1), 1.61)

    def test_km_to_miles(self):
        self.assertEqual(self.app.km_to_miles(1), 0.62)

    def test_miles_to_km_dict_type(self):
        with self.assertRaises(TypeError):
            self.app.miles_to_km({'a': 1, 'b': 2})

    def test_miles_to_km_list_type(self):
        with self.assertRaises(TypeError):
            self.app.miles_to_km([1, 2, 3])


if __name__ == '__main__':
    unittest.main()
