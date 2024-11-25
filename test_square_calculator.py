import unittest
from square_calculator import SquareCalculator

class TestSquareCalculator(unittest.TestCase):

    def setUp(self):
       
        self.square_calc = SquareCalculator()

    def test_area_positive(self):
       
        self.assertEqual(self.square_calc.area(5), 25)  # 5 * 5 = 25
        self.assertEqual(self.square_calc.area(10), 100)  # 10 * 10 = 100

    def test_area_zero(self):
       
        self.assertEqual(self.square_calc.area(0), 0)  # 0 * 0 = 0

    def test_area_negative(self):
        
        with self.assertRaises(ValueError):
            self.square_calc.area(-3)
        with self.assertRaises(ValueError):
            self.square_calc.area(-10)

if __name__ == '__main__':
    unittest.main()
