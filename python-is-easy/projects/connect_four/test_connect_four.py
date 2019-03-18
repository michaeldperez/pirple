import unittest

from connect_four import toggle_player

class TestConnectFour(unittest.TestCase):
    def test_toggle_player1(self):
        self.assertEqual(toggle_player(2), 1)
    
    def test_toggle_player2(self):
        self.assertEqual(toggle_player(1), 2)