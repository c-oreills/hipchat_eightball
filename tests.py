from unittest import TestCase

from roulette import pairwise_unique

class TestPairwiseUnique(TestCase):
    def test_pairwise_unique(self):
        iterator = iter([1, 1, 2, 2, 1, 2, 2, 2, 1, 1, 2])
        self.assertEqual(
                list(pairwise_unique(iterator)),
                [1, 2, 1, 2, 1, 2])

    def test_pairwise_unique_short(self):
        iterator = iter([1, 1])
        self.assertEqual(
                list(pairwise_unique(iterator)),
                [1,])

    def test_pairwise_unique_short_unique(self):
        iterator = iter([1, 2])
        self.assertEqual(
                list(pairwise_unique(iterator)),
                [1, 2,])
