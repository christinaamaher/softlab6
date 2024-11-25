# test_calculator.py

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        # This method is run before each test, useful for setup code.
        self.calc = Calculator()

    def test_power(self):
        # Test addition functionality
        result = self.calc.power(3,2)
        self.assertEqual(result, 9)
        
        result = self.calc.power(-1,6)
        self.assertEqual(result, 1)
        
        result = self.calc.power(5,0)
        self.assertEqual(result, 1)

if _name_ == '_main_':
    unittest.main()
