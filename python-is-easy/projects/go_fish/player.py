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
        card_indices = []
        removed_cards = []
        for idx, card in enumerate(self.hand_of_cards):
            if card == card_to_remove: # need to match rank
                card_indices.append(idx)
        for index in card_indices:
            removed_cards.append(
                self.hand_of_cards.pop(index)
            )
        return removed_cards