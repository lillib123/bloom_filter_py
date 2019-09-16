import unittest
from src.bloom_filter import BloomFilter


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.filter = BloomFilter()

    def test_validate_when_passed_a_letter_returns_its_place_in_alphabet(self):
        self.assertEqual(1, self.filter.validate('a'))
        self.assertEqual(13, self.filter.validate('m'))
        self.assertEqual(26, self.filter.validate('z'))

    def test_validate_is_case_insensitive(self):
        self.assertEqual(self.filter.validate('a'), self.filter.validate('A'))
        self.assertEqual(self.filter.validate('m'), self.filter.validate('M'))
        self.assertEqual(self.filter.validate('z'), self.filter.validate('Z'))

    def test_validate_when_passed_a_word_returns_sum_of_character_values(self):
        self.assertEqual(1630, self.filter.validate('cat'))
        self.assertEqual(2468, self.filter.validate('dog'))

    def test_add_word_to_filter_toggles_flag_at_array_index_n(self):
        self.filter.add_word('cat')
        self.assertTrue(self.filter.has_word('cat'))

    def test_has_word_returns_false_for_not_found_words(self):
        self.assertFalse(self.filter.has_word('sup'))

    def test_add_word_with_value_out_of_bounds_of_bloom_array_is_oooook(self):
        self.filter = BloomFilter()
        self.filter.add_word('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')

    def test_wordlist_loaded(self):
        self.filter.load_wordlist("../src/word_list.txt")
        self.assertTrue(len(self.filter.bloom_array) > 1)

    def test_find_word_in_wordlist_returns_true(self):
        self.filter.load_wordlist("../src/word_list.txt")
        self.assertTrue(self.filter.has_word("A'asia"))

    def test_find_word_not_in_wordlist_returns_false(self):
        self.filter.load_wordlist("../src/word_list.txt")
        self.assertFalse(self.filter.has_word("booooooo"))


if __name__ == '__main__':
    unittest.main()

