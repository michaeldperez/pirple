import unittest
import random
from typing import List
from card import Card
from hand_of_cards import HandOfCards
from player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        hand_of_cards: HandOfCards = HandOfCards()
        self.player: Player = Player(hand_of_cards)
        self.deck: List[Card] = [
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
        random.shuffle(self.deck)
        self.player.hand_of_cards.cards = [Card('K', '\u2663'), Card('10', '\u2665')]
    
    def test_add_cards(self):
        self.player.add_cards([Card('3', '\u2665'), Card('2', '\u2665'),  Card('A', '\u2665')])
        self.assertListEqual(
            [
                Card('K', '\u2663'), Card('10', '\u2665'), Card('3', '\u2665'), Card('2', '\u2665'),  Card('A', '\u2665')
            ],
            self.player.hand_of_cards.cards
        )
    
    def test_add_no_cards(self):
        self.player.add_cards([])
        self.assertListEqual([Card('K', '\u2663'), Card('10', '\u2665')], self.player.hand_of_cards.cards)
    
    def test_remove_cards(self):
        ten = self.player.remove_cards('10')
        self.assertListEqual(ten, [Card('10', '\u2665')])
    
    def test_remove_non_existant_cards(self):
        no_cards = self.player.remove_cards('9')
        self.assertListEqual(no_cards, [])

if __name__ == '__main__':
    unittest.main()