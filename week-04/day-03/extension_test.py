import unittest
import extension

class TestExtend(unittest.TestCase):

    def test_add_2_and_3_is_5(self):
        self.assertEqual(extension.add(2, 3), 5)

    def test_add_4_and_1_is_5(self):
        self.assertEqual(extension.add(4, 1), 5)

    def test_max_of_three_first(self):
        self.assertEqual(extension.max_of_three(5, 4, 3), 5)

    def test_max_of_three_third(self):
        self.assertEqual(extension.max_of_three(3, 6, 5), 6)

    def test_median_four(self):
        self.assertEqual(extension.median([7,6,3,4]), 6)

    def test_median_five(self):
        self.assertEqual(extension.median([1,2,7,4,5]), 7)

    def test_is_vowel_a(self):
        self.assertTrue(extension.is_vowel('a'))

    def test_is_vowel_u(self):
        self.assertTrue(extension.is_vowel('u'))

    def test_translate_bemutatkozik(self):
        self.assertEqual(extension.translate('bemutatkozik'), 'bevemuvutavatkovozivik')

    def test_translate_kolbice(self):
        self.assertEqual(extension.translate('kolbice'), 'kovolbiviceve')

if __name__ == '__main__':
    unittest.main()