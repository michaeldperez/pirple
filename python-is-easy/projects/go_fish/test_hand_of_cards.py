import unittest
from typing import List
from card import Card
from hand_of_cards import HandOfCards

class TestHandOfCards(unittest.TestCase):
    def setUp(self):
        self.hand: HandOfCards = HandOfCards()
    
    def test_add_cards(self):
        cards = [Card('3', '\u2665'), Card('2', '\u2665'),  Card('A', '\u2665')]
        self.hand.add_cards(cards)
        self.assertListEqual(self.hand.cards, cards)
    
    def test_remove_cards_when_empty(self):
        empty_cards = self.hand.remove_cards('10')
        self.assertListEqual(empty_cards, [])
    
    def test_remove_non_existant_cards(self):
        self.hand.cards = [
            Card('3', '\u2665'), Card('2', '\u2665'),  Card('A', '\u2665')
        ]
        no_cards = self.hand.remove_cards('7')
        self.assertListEqual(no_cards, [])
    
    def test_remove_existant_cards(self):
        self.hand.cards = [
            Card('3', '\u2665'), Card('2', '\u2665'),  Card('A', '\u2665'), \
            Card('3', '\u2660')
        ]
        threes = self.hand.remove_cards('3')
        self.assertListEqual(threes, [Card('3', '\u2665'), Card('3', '\u2660')])
        self.assertListEqual(self.hand.cards, [Card('2', '\u2665'),  Card('A', '\u2665')])

if __name__ == '__main__':
    unittest.main()