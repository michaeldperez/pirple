import unittest
from typing import List
from card import Card
from deck import Deck

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.new_deck : List[Card] = [
            Card('K', '\u2663'),  Card('Q', '\u2663'),  Card('J', '\u2663'),  Card('10', '\u2663'),
            Card('9', '\u2663'),  Card('8', '\u2663'),  Card('7', '\u2663'),  Card('6', '\u2663'),
            Card('5', '\u2663'),  Card('4', '\u2663'),  Card('3', '\u2663'),  Card('2', '\u2663'),
            Card('A', '\u2663'),  Card('K', '\u2660'),  Card('Q', '\u2660'),  Card('J', '\u2660'),
            Card('10', '\u2660'), Card('9', '\u2660'),  Card('8', '\u2660'),  Card('7', '\u2660'),
            Card('6', '\u2660'),  Card('5', '\u2660'),  Card('4','\u2660'),   Card('3', '\u2660'),
            Card('2', '\u2660'),  Card('A', '\u2660'),  Card('K', '\u2666'),  Card('Q', '\u2666'), 
            Card('J', '\u2666'),  Card('10', '\u2666'), Card('9', '\u2666'),  Card('8', '\u2666'),
            Card('7', '\u2666'),  Card('6', '\u2666'),  Card('5', '\u2666'),  Card('4', '\u2666'),
            Card('3', '\u2666'),  Card('2', '\u2666'),  Card('A', '\u2666'),  Card('K', '\u2665'),
            Card('Q', '\u2665'),  Card('J', '\u2665'),  Card('10', '\u2665'), Card('9', '\u2665'),
            Card('8', '\u2665'),  Card('7', '\u2665'),  Card('6', '\u2665'),  Card('5', '\u2665'),
            Card('4', '\u2665'),  Card('3', '\u2665'),  Card('2', '\u2665'),  Card('A', '\u2665')
        ]
        self.deck = Deck()
    
    def test_create(self):
        self.deck.create()
        self.assertListEqual(self.deck.cards, self.new_deck)
    
    def test_setter(self):
        self.assertListEqual(self.deck.cards, [])
        self.deck.cards = self.new_deck
        self.assertListEqual(self.deck.cards, self.new_deck)
    
    def test_shuffle(self):
        self.deck.create()
        self.deck.shuffle()
        self.assertNotEqual(self.deck.cards, self.new_deck)
        self.assertEqual(len(self.deck.cards), 52)
    
    def test_draw_hand(self):
        self.deck.create()
        hand = self.deck.draw(7)
        self.assertListEqual([
            Card('A', '\u2665'), Card('2', '\u2665'), Card('3', '\u2665'),
            Card('4', '\u2665'), Card('5', '\u2665'), Card('6', '\u2665'),
            Card('7', '\u2665'),
        ], hand)

    def test_draw_negative_cards(self):
        self.deck.create()
        self.deck.shuffle()
        with self.assertRaises(ValueError) as cm:
            self.deck.draw(-1)
        self.assertEqual(
            'Number of cards drawn must be positive: -1',
            str(cm.exception)
        )

    def test_draw_too_many_cards(self):
        self.deck.create()
        self.deck.shuffle()
        for _ in range(0, 4):
            self.deck.draw(13)
        with self.assertRaises(IndexError) as cm:
            self.deck.draw(1)
        self.assertEqual(
            '1 is greater than the current number of cards: 0',
            str(cm.exception)
        )

if __name__ == '__main__':
    unittest.main()