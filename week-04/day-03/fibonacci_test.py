import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_one(self):
        self.assertEqual(fibonacci(1), 1)

    def test_two(self):
        self.assertNotEqual(fibonacci(2), 3)

    def test_twenty(self):
        self.assertNotEqual(fibonacci(20), 40)


if __name__ == '__main__':
    unittest.main()