import unittest
from average import calculate_average

class TestCalculateAverage(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(calculate_average([10, 20, 30]), 20)

    def test_negative_numbers(self):
        self.assertEqual(calculate_average([-1, -2, -3]), -2)

    def test_empty_list(self):
        self.assertIsNone(calculate_average([]))

if __name__ == '__main__':
    unittest.main()