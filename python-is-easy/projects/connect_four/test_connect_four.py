import unittest

from connect_four import toggle_player, player_icon, able_to_move

class TestConnectFour(unittest.TestCase):
    def setUp(self):
        self.board = [
            [' ', ' ', ' ', ' ', 'X', ' ', ' '],
            [' ', ' ', ' ', ' ', 'O', ' ', ' '],
            [' ', ' ', ' ', ' ', 'X', ' ', ' '],
            [' ', ' ', ' ', ' ', 'O', ' ', ' '],
            [' ', 'O', ' ', ' ', 'X', ' ', ' '],
            [' ', 'X', ' ', ' ', 'O', ' ', ' '],
            [' ', 'X', ' ', ' ', 'X', ' ', ' ']
        ]
    def tearDown(self):
        pass

    def test_toggle_player1(self):
        self.assertEqual(toggle_player(2), 1)
    
    def test_toggle_player2(self):
        self.assertEqual(toggle_player(1), 2)

    def test_player_one_icon(self):
        self.assertEqual(player_icon(1), 'X')
    
    def test_player_two_icon(self):
        self.assertEqual(player_icon(2), 'O')
    
    def test_able_to_move(self):
        self.assertTrue(able_to_move(self.board, 1))
    
    def test_not_able_to_move(self):
        self.assertFalse(able_to_move(self.board, 4))

if __name__ == '__main__':
    unittest.main()