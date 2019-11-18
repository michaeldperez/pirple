from typing import List 
from card import Card

class HandOfCards:
    def __init__(self):
        self._cards: List[Card] = []
    
    @property
    def cards(self) -> List[Card]:
        return self._cards
    
    @cards.setter
    def cards(self, cards: List[Card]) -> None:
        self._cards = cards
    
    def add_cards(self, cards_to_add: List[Card]) -> None:
        self.cards.extend(cards_to_add)
    
    def remove_cards(self, card_to_remove: str) -> List[Card]:
        cards = [
            card for card in self.cards if card.rank == card_to_remove
        ]
        self.cards = [
            card for card in self.cards if card.rank != card_to_remove
        ]
        return cards