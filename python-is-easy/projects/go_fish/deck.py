import random
from typing import List
from card import Card

class Deck:
    suits = [
        "\u2663", # club
        "\u2660", # spade
        "\u2666", # diamond
        "\u2665"  # heart
    ]

    ranks = [
        'K', 'Q', 'J', '10', 
        '9', '8', '7', '6', 
        '5', '4', '3', '2', 'A'
    ]
 
    def __init__(self):
        self._cards: List[Card] = []
    
    @property
    def cards(self) -> List[Card]:
        return self._cards
    
    @cards.setter
    def cards(self, cards: List[Card]) -> None:
        self._cards = cards

    def create(self) -> None:
        if len(self.cards) == 0:
            for suit in Deck.suits:
                for rank in Deck.ranks:
                    self.cards.append(Card(rank, suit))
    
    def shuffle(self) -> None:
        random.shuffle(self.cards)
    
    def draw(self, n) -> List[Card]:
        number_of_cards: int = len(self.cards)
        if n <= 0:
            raise ValueError(f'Number of cards drawn must be positive: {n}')
        elif n <= number_of_cards and number_of_cards <= 52:
           return [self.cards.pop() for _ in range(0,n)]
        else:
            raise IndexError(f'{n} is greater than the current number of cards: {number_of_cards}')
