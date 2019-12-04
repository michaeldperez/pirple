from typing import List
from card import Card
from deck import Deck

class Dealer:
    def __init__(self, deck: Deck):
        self.deck = deck
        self.prepare_deck()
    
    def prepare_deck(self) -> None:
        self.deck.create()
        self.deck.shuffle()
    
    def deal_cards(self, number_of_cards: int) -> List[Card]:
        try:
            cards = self.deck.draw(number_of_cards)
            return cards
        except ValueError as ve_err:
            print(str(ve_err))
            return []
        except IndexError as idx_err:
            print(str(idx_err))
            return []
