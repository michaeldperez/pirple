class HangmanPlayer:
    def __init__(self, id):
        self.id = id
        self.incorrect_guesses = 0
    
    def increment_incorrect_guesses(self):
        self.incorrect_guesses += 1
    
    def number_of_incorrect_guesses(self):
        return self.incorrect_guesses