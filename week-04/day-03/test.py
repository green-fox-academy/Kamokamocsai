import unittest
from prime import is_prime

class PrimeTestCases(unittest.TestCase):
    def test_three(self):
        self.assertTrue(is_prime(3))

if __name__ == '__main__':
    unittest.main()