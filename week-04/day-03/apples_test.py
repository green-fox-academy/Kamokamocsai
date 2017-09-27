import unittest
from apples import Apple

test_apple = Apple()

class GetAppleTest(unittest.TestCase):

    def test_get_apple(self):        
        self.assertEqual(test_apple.get_apple(), "apple")

    def test_get_apple(self):        
        self.assertEqual(test_apple.get_apple(), "bananas")


if __name__ == '__main__':
    unittest.main()