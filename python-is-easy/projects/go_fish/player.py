class Player:
    def __init__(self):
        self._hand_of_cards = []
    
    @property
    def hand_of_cards(self):
        return self._hand_of_cards
    
    @hand_of_cards.setter
    def hand_of_cards(self, hand):
        self._hand_of_cards = hand
    
    def add_cards(self, cards_to_add):
        self.hand_of_cards.extend(cards_to_add)
    
    def remove_cards(self, card_to_remove):
        return list(
            filter(
                lambda card: card_to_remove in card, 
                self.hand_of_cards
            )
        )
