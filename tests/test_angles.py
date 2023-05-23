import math
import unittest
from your_library.angles import sin, cos, tan

class TestAngles(unittest.TestCase):
    def test_sin(self):
        self.assertAlmostEqual(sin(math.pi/6), 0.5)
        self.assertAlmostEqual(sin(math.pi/4), math.sqrt(2)/2)
        # Add more test cases for sin function

    def test_cos(self):
        self.assertAlmostEqual(cos(math.pi/3), 0.5)
        self.assertAlmostEqual(cos(math.pi/4), math.sqrt(2)/2)
        # Add more test cases for cos function

    def test_tan(self):
        self.assertAlmostEqual(tan(math.pi/6), math.sqrt(3)/3)
        self.assertAlmostEqual(tan(math.pi/4), 1)
        # Add more test cases for tan function

if __name__ == '__main__':
    unittest.main()
