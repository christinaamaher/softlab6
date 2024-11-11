# test_square_calculator.py

import unittest
from square_calculator import SquareCalculator

class TestSquareCalculator(unittest.TestCase):

    def setUp(self):
        # Initialize an instance of SquareCalculator before each test
        self.square_calc = SquareCalculator()

    def test_area(self):
        # Test area calculation for a positive side length
        result = self.square_calc.area(5)
        self.assertEqual(result, 25)  # 5 * 5 = 25
        
        result = self.square_calc.area(0)
        self.assertEqual(result, 0)  # 0 * 0 = 0
        
        # Test area calculation for a negative side length, expecting a ValueError
        with self.assertRaises(ValueError):
            self.square_calc.area(-3)

if __name__ == '__main__':
    unittest.main()
