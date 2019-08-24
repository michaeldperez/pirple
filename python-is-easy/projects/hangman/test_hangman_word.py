import unittest
from unittest.mock import MagicMock
from hangman_word import HangmanWord

class HangmanWordTest(unittest.TestCase):
    def setUp(self):
        self.hangman_word = HangmanWord("hello")
    
    def test_check_when_true(self):
        self.hangman_word._contains = MagicMock(name="contains")
        self.hangman_word._contains.return_value = True
        self.hangman_word._find_indices = MagicMock(name="find")
        self.hangman_word._find_indices.return_value = [4]
        indicies = self.hangman_word.check("o")
        self.hangman_word._contains.assert_called_with("hello", "o")
        self.hangman_word._find_indices.assert_called_with("hello", "o")
        self.assertListEqual(indicies, [4])
    
    def test_check_when_false(self):
        self.hangman_word._contains = MagicMock(name="contains")
        self.hangman_word._contains.return_value = False
        indices = self.hangman_word.check("x")
        self.hangman_word._contains.assert_called_with("hello", "x") 
        self.assertIsNone(indices)

if __name__ == "__main__":
    unittest.main()