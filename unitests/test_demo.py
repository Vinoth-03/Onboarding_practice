import unittest
from app import calculate_area, calculate_perimeter

class TestSquareCalculator(unittest.TestCase):

    def test_calculate_area_positive(self):
        self.assertEqual(calculate_area(5), 25)
        self.assertEqual(calculate_area(0), 0)
        self.assertAlmostEqual(calculate_area(2.5), 6.25)

    def test_calculate_area_negative(self):
        self.assertEqual(calculate_area(-4), 16)  # (-4)^2 = 16

    def test_calculate_perimeter_positive(self):
        self.assertEqual(calculate_perimeter(5), 20)
        self.assertEqual(calculate_perimeter(0), 0)
        self.assertAlmostEqual(calculate_perimeter(2.5), 10.0)

    def test_calculate_perimeter_negative(self):
        self.assertEqual(calculate_perimeter(-4), -16)  # May depend on expected behavior

if __name__ == '__main__':
    unittest.main()
