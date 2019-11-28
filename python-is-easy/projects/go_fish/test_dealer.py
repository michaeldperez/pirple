import unittest

from typing import List
from card import Card
from deck import Deck
from dealer import Dealer

class TestDealer(unittest.TestCase):
    def setUp(self):
        self.unshuffled_deck: List[Card] = [
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
        deck: Deck = Deck()
        self.dealer: Dealer = Dealer(deck)

    def test_prepare_deck(self):
        self.dealer.prepare_deck()
        self.assertNotEqual(self.dealer.deck, self.unshuffled_deck)
    
    def test_deal_cards(self):
        self.dealer.prepare_deck()
        cards = self.dealer.deal_cards(5)
        self.assertTrue(
            all(isinstance(card, Card) for card in cards)
        )
        self.assertEqual(len(cards), 5)
    def test_negative_deal_cards(self):
        pass

    def test_too_many_deal_cards(self):
        pass


if __name__ == '__main__':
    unittest.main()