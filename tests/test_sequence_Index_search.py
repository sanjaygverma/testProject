from unittest import TestCase

from sequence_Index_search import SequenceIndexSearch


class TestSequenceIndexSearch(TestCase):

    def setUp(self):
        self.seq_search = SequenceIndexSearch()

    def test_1_index_longest_sequence(self):
        self.assertEqual(self.seq_search.index_longest_sequence(156),4)

    def test_2_index_longest_sequence(self):
        self.assertEqual(self.seq_search.index_longest_sequence(9223372036854775800),1)

    def test_3_index_longest_sequence(self):
        self.assertEqual(self.seq_search.index_longest_sequence(88), 3)



