import unittest
from hangman_player import HangmanPlayer

class HangmanPlayerTest(unittest.TestCase):
    def setUp(self):
        self.hangman_player = HangmanPlayer(1)

    def test_increment_guesses(self):
        self.hangman_player.increment_incorrect_guesses()
        self.assertEqual(self.hangman_player.incorrect_guesses, 1)
    
    def test_number_of_incorrect_guesses(self):
        self.hangman_player.incorrect_guesses = 5
        self.assertEqual(self.hangman_player.number_of_incorrect_guesses(), 5)

if __name__ == "__main__":
    unittest.main()