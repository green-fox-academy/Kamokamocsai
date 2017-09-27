import unittest
from anagram import Anagram

test_anagram = Anagram()

class AnagramTest(unittest.TestCase):

    def test_anagram(self):
        self.assertEqual(test_anagram.anagram("tejet", "tejet"), True)

    def test_anagram(self):
        self.assertNotEqual(test_anagram.anagram("tejet", "tejet"), False)

    
if __name__ == '__main__':
    unittest.main()