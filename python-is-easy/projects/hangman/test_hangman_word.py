import unittest
from unittest.mock import MagicMock
from hangman_word import HangmanWord

class HangmanWordTest(unittest.TestCase):
    def setUp(self):
        self.hangman_word = HangmanWord("hello")
    
    def test_check_when_true_and_complete(self):
        self.hangman_word.obfuscated_word = "hell_"
        self.hangman_word._contains = MagicMock(name="contains")
        self.hangman_word._contains.return_value = True
        self.hangman_word._find_indices = MagicMock(name="find")
        self.hangman_word._find_indices.return_value = [4]
        self.hangman_word._reveal = MagicMock(name="reveal")
        self.hangman_word._reveal.return_value = "hello"
        self.hangman_word._discovered = MagicMock(name="discovered")
        self.hangman_word._discovered.return_value = True
        letter_exists, is_discovered  = self.hangman_word.check("o")
        self.hangman_word._contains.assert_called_with("hello", "o")
        self.hangman_word._find_indices.assert_called_with("hello", "o")
        self.hangman_word._reveal.assert_called_with("o", [4], "hell_")
        self.hangman_word._discovered.assert_called_with("hello", "hello")
        self.assertTrue(letter_exists)
        self.assertTrue(is_discovered)
    
    def test_when_true_and_incomplete(self):
        self.hangman_word._contains = MagicMock(name="contains")
        self.hangman_word._contains.return_value = True
        self.hangman_word._find_indices = MagicMock(name="find")
        self.hangman_word._find_indices.return_value = [2, 3]
        self.hangman_word._reveal = MagicMock(name="reveal")
        self.hangman_word._reveal.return_value = "__ll_"
        self.hangman_word._discovered = MagicMock(name="discovered")
        self.hangman_word._discovered.return_value = False
        letter_exists, is_discovered  = self.hangman_word.check("l")
        self.hangman_word._contains.assert_called_with("hello", "l")
        self.hangman_word._find_indices.assert_called_with("hello", "l")
        self.hangman_word._reveal.assert_called_with("l", [2,3], "_____")
        self.hangman_word._discovered.assert_called_with("hello", "__ll_")
        self.assertTrue(letter_exists)
        self.assertFalse(is_discovered)
    
    def test_check_when_false(self):
        self.hangman_word._contains = MagicMock(name="contains")
        self.hangman_word._contains.return_value = False
        letter_exists, is_discovered = self.hangman_word.check("x")
        self.hangman_word._contains.assert_called_with("hello", "x")
        self.assertFalse(letter_exists)
        self.assertFalse(is_discovered)

if __name__ == "__main__":
    unittest.main()