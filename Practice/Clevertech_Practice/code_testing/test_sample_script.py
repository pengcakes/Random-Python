import unittest
from sample_script import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # when r > 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi*2.1**2)
    def test_values(self):
        # make sure value errors are being raised.
        # (exception class to be raised, function, arguments to function)
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        # make sure type errors are raised
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
