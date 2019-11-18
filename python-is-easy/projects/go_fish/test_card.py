import unittest
import typing

from card import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card('A', '\u2660')
    
    def test_get_rank(self):
        self.assertEqual('A', self.card.rank)
    
    def test_set_rank(self):
        self.card.rank = 'J'
        self.assertEqual('J', self.card.rank)
    
    def test_get_suite(self):
        self.assertEqual('\u2660', self.card.suite)
    
    def test_set_suite(self):
        self.card.suite = '\u2663'
        self.assertEqual('\u2663', self.card.suite)
    
    def test_str_method(self):
        self.assertEqual(str(self.card), 'A\u2660')
    
    def test_equality(self):
        self.assertEqual(self.card, Card('A', '\u2660'))
    
if __name__ == '__main__':
    unittest.main()