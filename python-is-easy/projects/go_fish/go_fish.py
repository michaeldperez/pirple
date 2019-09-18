from deck import Deck
from player import Player

class GoFish:
    def __init__(self):
        self.player = Player()
        self.deck = Deck()
        self.prepare_deck(self.deck)
    
    def prepare_deck(self, deck):
        deck.create()
        deck.shuffle()

    def play(self):
        pass