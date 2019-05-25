import unittest

#from connect_four import toggle_player, player_icon, able_to_move, check_column
import connect_four as cf
class TestConnectFour(unittest.TestCase):
    def setUp(self):
        self.board = [
            [' ', ' ', ' ', ' ', 'X', ' ', 'O'],
            [' ', ' ', ' ', ' ', 'O', ' ', 'X'],
            [' ', ' ', ' ', ' ', 'X', ' ', 'O'],
            [' ', ' ', 'X', ' ', 'O', ' ', 'O'],
            [' ', 'O', 'X', ' ', 'X', ' ', 'O'],
            [' ', 'X', 'X', ' ', 'O', ' ', 'X'],
            [' ', 'X', 'X', ' ', 'X', ' ', 'X']
        ]
    def tearDown(self):
        pass

    def test_toggle_player1(self):
        self.assertEqual(cf.toggle_player(2), 1)
    
    def test_toggle_player2(self):
        self.assertEqual(cf.toggle_player(1), 2)

    def test_player_one_icon(self):
        self.assertEqual(cf.player_icon(1), 'X')
    
    def test_player_two_icon(self):
        self.assertEqual(cf.player_icon(2), 'O')
    
    def test_able_to_move(self):
        self.assertTrue(cf.able_to_move(self.board, 1))
    
    def test_not_able_to_move(self):
        self.assertFalse(cf.able_to_move(self.board, 4))
    
    def test_check_column_not_win(self):
        self.assertFalse(cf.check_column(self.board, 6, 'O'))
    
    def test_check_column_win(self):
        self.assertTrue(cf.check_column(self.board, 2, 'X'))

if __name__ == '__main__':
    unittest.main()