from typing import List
from deck import Deck

class Dealer:
    def __init__(self, deck: Deck):
        self.deck = deck
        self.prepare_deck(self.deck)
    
    def prepare_deck(self, deck: Deck) -> None:
        deck.create()
        deck.shuffle()
    
    def deal_cards(self, deck: Deck, number_of_cards: int) -> List[str]:
        return deck.draw(number_of_cards)