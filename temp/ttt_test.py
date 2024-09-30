import unittest
from unittest import mock
from io import StringIO  # Import StringIO from io
from tic_tac_toe import print_board, check_win, get_player_move, play_game

class TicTacToeTest(unittest.TestCase):

    def test_print_board(self):
        board = [["X", "O", " "], [" ", "X", "O"], ["O", " ", "X"]]
        expected_output = """---------
| X | O |   |
---------
|   | X | O |
---------
| O |   | X |
---------"""
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            print_board(board)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_check_win_row(self):
        board = [["X", "X", "X"], [" ", "O", " "], ["O", " ", " "]]
        self.assertEqual(check_win(board), "X")

    def test_check_win_column(self):
        board = [["X", "O", " "], ["X", "O", " "], ["X", " ", " "]]
        self.assertEqual(check_win(board), "X")

    def test_check_win_diagonal(self):
        board = [["X", "O", " "], [" ", "X", " "], [" ", " ", "X"]]
        self.assertEqual(check_win(board), "X")

    def test_check_win_no_winner(self):
        board = [["X", "O", " "], [" ", " ", " "], ["O", "X", " "]]
        self.assertIsNone(check_win(board))

    def test_get_player_move_valid(self):
        board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        with unittest.mock.patch('builtins.input', return_value="1 2"):
            row, col = get_player_move(board, "1 2")
            self.assertEqual(row, 0)
            self.assertEqual(col, 1)

    def test_get_player_move_invalid_input(self):
        board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        with unittest.mock.patch('builtins.input', side_effect=["abc", "1 4", "1 2"]):
            row, col = get_player_move(board, "1 2")
            self.assertEqual(row, 0)
            self.assertEqual(col, 1)

    def test_get_player_move_occupied_cell(self):
        board = [["X", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        with unittest.mock.patch('builtins.input', return_value="1 1"):
            row, col = get_player_move(board, "1 1")
            self.assertNotEqual(row, 0)
            self.assertNotEqual(col, 0)

    @unittest.mock.patch('builtins.input', side_effect=["1 1", "2 2", "3 3", "1 2", "2 1", "3 1"])
    def test_play_game_x_wins(self, mock_input):
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            play_game()
            self.assertIn("Player X wins!", mock_stdout.getvalue())

    @unittest.mock.patch('builtins.input', side_effect=["1 1", "2 2", "1 2", "3 3", "2 1", "3 2", "1 3"])
    def test_play_game_draw(self, mock_input):
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            play_game()
            self.assertIn("It's a draw!", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()