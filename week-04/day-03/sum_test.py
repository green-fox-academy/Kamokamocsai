import unittest
from summ import SumNumbers

test_summ = SumNumbers()

class SumNumbersTest(unittest.TestCase):
    
    def test_empty(self):
        self.assertEqual(test_summ.sum_numbers([]), 0)

    def test_empty(self):
        self.assertEqual(test_summ.sum_numbers([1, 3, 6]), 10)

    def test_empty(self):
        self.assertNotEqual(test_summ.sum_numbers([2, 2]), 5)


if __name__ == '__main__':
    unittest.main()