import random

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
        self.cards = []
    
    def create(self):
        for suit in Deck.suits:
            for rank in Deck.ranks:
                self.cards.append(f'{rank}{suit}')
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self, n):
        number_of_cards = len(self.cards)
        if n <= 0:
            raise ValueError(f'Number of cards drawn must be positive: {n}')
        elif n <= number_of_cards:
           return [self.cards.pop() for _ in range(0,n)]
        else:
            raise IndexError(f'{n} is greater than the current number of cards: {number_of_cards}')
