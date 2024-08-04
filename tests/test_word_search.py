import timeit
import unittest
from unittest import TestCase
from word_search import WordSearch


class TestWordSearch(TestCase):

    def setUp(self):
        self.word_search = WordSearch()

    def test_1_find_word(self):
        self.assertEqual(self.word_search.find_word("I Love You & I care for You", "I"), "I")

    # test case 2
    def test_2_find_word(self):
        self.assertEqual(self.word_search.find_word("My Lovely You & I care for You", "e"), "Lovely")

    # test case 3
    def test_3_find_word(self):
        self.assertEqual(self.word_search.find_word("case sensitive letter I comes only once", "I"), "I")

    # test case 3
    def test_4_find_word(self):
        self.assertEqual(self.word_search.find_word(
            "This is a very long sentence and I want to educate everyone in this whole crazy world", "z"),
            "crazy")

    def test_5_find_word(self):
        self.assertEqual(self.word_search.find_word("Both Sentence and everyone have 3 occurrences of letter e "
                                                    "and total length of the words are 8 but sentence occurred first "
                                                    "in the input so the expected result in sentence", "e")
                         , "Sentence")

    def test_6_find_word(self):
        self.assertEqual(self.word_search.find_word(
            "Both sentence and everyone have 3 occurrences of letter e and total length of the words are 8 but "
            "sentence occurred first in the input so the expected result in sentence, this is excellence",
            "e"), "excellence")


    def test_7_find_word(self):
        self.assertEqual(self.word_search.find_word("Ha ha ha ha 88888 oooofh", "H"), "Ha")

    def test_8_find_word(self):
        self.assertEqual(self.word_search.find_word("Ha ha ha ha 88888 oooofh", "8"), "88888")

    def test_performance_word(self):
        time = timeit.timeit(self.util,  number=10000000)
        print(f" total run {time} time")

    def util(self):
        self.word_search.find_word(
            "Both sentence and everyone have 3 occurrences of letter e and total length of the words are 8 but "
            "sentence occurred first in the input so the expected result in sentence, this is excellence",
        "e")


if __name__ == "__main__":
    unittest.main()
