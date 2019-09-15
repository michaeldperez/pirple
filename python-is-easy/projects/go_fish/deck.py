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