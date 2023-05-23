import math
import unittest
from your_library.conversions import deg_to_rad, rad_to_deg

class TestConversions(unittest.TestCase):
    def test_deg_to_rad(self):
        self.assertAlmostEqual(deg_to_rad(45), math.pi/4)
        self.assertAlmostEqual(deg_to_rad(90), math.pi/2)
        # Add more test cases for deg_to_rad function

    def test_rad_to_deg(self):
        self.assertAlmostEqual(rad_to_deg(math.pi/6), 30)
        self.assertAlmostEqual(rad_to_deg(math.pi/2), 90)
        # Add more test cases for rad_to_deg function

if __name__ == '__main__':
    unittest.main()
