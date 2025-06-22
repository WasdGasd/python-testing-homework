import unittest
from main import calculate_average

class TestCalculateAverage(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(calculate_average([2, 4, 6]), 4)

    def test_negative_numbers(self):
        self.assertEqual(calculate_average([-3, -6, -9]), -6)

    def test_empty_list(self):
        self.assertIsNone(calculate_average([]))

if __name__ == '__main__':
    unittest.main()
