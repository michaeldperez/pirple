import unittest
import connect_four as cf

class TestConnectFour(unittest.TestCase):
    def setUp(self):
        self.board = [
            [' ', ' ', ' ', ' ', 'X', ' ', 'O'],
            [' ', ' ', ' ', ' ', 'O', ' ', 'X'],
            [' ', ' ', 'X', ' ', 'X', ' ', 'O'],
            [' ', ' ', 'X', 'X', 'O', ' ', 'O'],
            [' ', 'O', 'X', 'O', 'X', ' ', 'O'],
            ['X', 'X', 'X', 'X', 'X', 'O', 'X']
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
    
    def test_check_row_not_win(self):
        self.assertFalse(cf.check_row(self.board, 4, 'X'))
    
    def test_check_row_win(self):
        self.assertTrue(cf.check_row(self.board, 5, 'X'))
    
    def test_check_all_columns_true(self):
        self.assertTrue(cf.check_all(self.board, 'X', cf.check_column))
    
    def test_check_all_columns_false(self):
        self.assertFalse(cf.check_all(self.board, 'O', cf.check_column))
    
    def test_check_all_rows_true(self):
        self.assertTrue(cf.check_all(self.board, 'X', cf.check_row))
    
    def test_check_all_rows_false(self):
        self.assertFalse(cf.check_all(self.board, 'O', cf.check_row))
    
    def test_check_in_bounds_top_left(self):
        self.assertTrue(cf.check_in_bounds(0, 0))
    
    def test_check_in_bounds_bottom_right(self):
        self.assertTrue(cf.check_in_bounds(5, 6))
    
    def test_check_out_bounds_row(self):
        self.assertFalse(cf.check_in_bounds(7, 6))
    
    def test_check_out_bounds_column(self):
        self.assertFalse(cf.check_in_bounds(4, 8))

    def test_check_diag_true(self):
        self.assertTrue(cf.check_diag(self.board, 4, 2, 'X'))
    
    def test_check_diag_false(self):
        self.assertFalse(cf.check_diag(self.board, 4, 3, 'O'))

if __name__ == '__main__':
    unittest.main()