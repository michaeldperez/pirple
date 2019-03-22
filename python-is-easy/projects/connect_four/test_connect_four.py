import unittest

from connect_four import toggle_player, player_icon

class TestConnectFour(unittest.TestCase):
    def test_toggle_player1(self):
        self.assertEqual(toggle_player(2), 1)
    
    def test_toggle_player2(self):
        self.assertEqual(toggle_player(1), 2)

    def test_player_one_icon(self):
        self.assertEqual(player_icon(1), 'X')
    
    def test_player_two_icon(self):
        self.assertEqual(player_icon(2), 'O')