from typing import List
from card import Card
from hand_of_cards import HandOfCards

class Player:
    def __init__(self, hand_of_cards: HandOfCards):
        self._hand_of_cards: HandOfCards = hand_of_cards

    @property
    def hand_of_cards(self) -> HandOfCards:
        return self._hand_of_cards
    
    @hand_of_cards.setter
    def hand_of_cards(self, hand: HandOfCards) -> None:
        self._hand_of_cards = hand
    
    def add_cards(self, cards_to_add: List[Card]) -> None:
        self.hand_of_cards.add_cards(cards_to_add)
    
    def remove_cards(self, card_to_remove: str) -> List[Card]:
        return self.hand_of_cards.remove_cards(card_to_remove)
