import unittest
from counter import letter_counter

class LetterCounterTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(letter_counter(''), {})
    
    def test_one_letter(self):
        self.assertEqual(letter_counter("a"), {"a": 1})
        self.assertEqual(letter_counter("b"), {"b": 1})

    def test_two_different_letters(self):
        self.assertEqual(letter_counter("ab"), {"a": 1, "b": 1})

    def test_two_same_letters(self):
        self.assertEqual(letter_counter("aa"), {"a": 2})
        

if __name__ == '__main__':
    unittest.main()