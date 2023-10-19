import unittest
from impl.izboard import IzBoard
from board import Piece

class TestIzBoard(unittest.TestCase):

    def test_insert_piece_valid_move_on_left_doesnt_throw_error(self):
        board = IzBoard()
        board.insert_piece(0)

    def test_insert_piece_valid_move_on_right_doesnt_throw_error(self):
        board = IzBoard()
        board.insert_piece(6)

    def test_insert_piece_invalid_negative_move_ends_game(self):
        board = IzBoard()

        board.insert_piece(-1)

        self.assertTrue(board.is_gameover())

    def test_insert_piece_invalid_positive_move_ends_game(self):
        board = IzBoard()

        board.insert_piece(10)

        self.assertTrue(board.is_gameover())

    def test_insert_piece_invalid_move_just_outside_board_ends_game(self):
        board = IzBoard()

        board.insert_piece(7)

        self.assertTrue(board.is_gameover())

    def test_insert_piece_invalid_move_player_loses(self):
        board = IzBoard()
        player = board.current_player()
        other = other_player(player)

        board.insert_piece(-1)

        self.assertNotEqual(board.get_winner(), other)

    def test_insert_piece_changes_current_player(self):
        board = IzBoard()
        player = board.current_player()
        other = other_player(player)

        board.insert_piece(0)

        self.assertEqual(board.current_player(), other)

    def test_get_piece_returns_empty_at_start(self):
        board = IzBoard()
        for x in range(7):
            for y in range(6):
                self.assertEqual(board.get_piece(x, y), Piece.EMPTY)

    def test_insert_piece_two_moves_returns_to_first_player(self):
        board = IzBoard()
        player = board.current_player()

        board.insert_piece(0)
        board.insert_piece(1)

        self.assertEqual(board.current_player(), player)

    def test_insert_piece_get_piece_returns_correct_piece(self):
        board = IzBoard()
        player = board.current_player()

        board.insert_piece(0)

        self.assertEqual(board.get_piece(0, 6), player)

    def test_insert_piece_get_piece_two_pieces_returns_correct_piece(self):
        board = IzBoard()
        player = board.current_player()

        board.insert_piece(0)
        board.insert_piece(1)

        self.assertEqual(board.get_piece(0, 6), player)

    def test_insert_piece_get_piece_full_row_returns_correct_pieces(self):
        board = IzBoard()
        player = board.current_player()
        other = other_player(player)

        board.insert_piece(0)
        board.insert_piece(1)
        board.insert_piece(2)
        board.insert_piece(3)
        board.insert_piece(4)
        board.insert_piece(5)
        board.insert_piece(6)

        self.assertEqual(board.get_piece(0, 6), player)
        self.assertEqual(board.get_piece(1, 6), other)
        self.assertEqual(board.get_piece(2, 6), player)
        self.assertEqual(board.get_piece(3, 6), other)
        self.assertEqual(board.get_piece(4, 6), player)
        self.assertEqual(board.get_piece(5, 6), other)
        self.assertEqual(board.get_piece(6, 6), player)

    def test_insert_piece_get_piece_full_column_returns_correct_pieces(self):
        board = IzBoard()
        player = board.current_player()
        other = other_player(player)

        board.insert_piece(0)
        board.insert_piece(0)
        board.insert_piece(0)
        board.insert_piece(0)
        board.insert_piece(0)
        board.insert_piece(0)

        self.assertEqual(board.get_piece(0, 5), player)
        self.assertEqual(board.get_piece(0, 4), other)
        self.assertEqual(board.get_piece(0, 3), player)
        self.assertEqual(board.get_piece(0, 2), other)
        self.assertEqual(board.get_piece(0, 1), player)
        self.assertEqual(board.get_piece(0, 0), other)

    def test_insert_piece_column_already_full_ends_game(self):
        board = IzBoard()

        # Fill the column
        for _ in range(6):
            board.insert_piece(0)

        player = board.current_player()
        other_player = other_player(player)
        board.insert_piece(0)

        self.assertTrue(board.is_gameover())
        self.assertTrue(board.get_winner(), other_player)

    def test_insert_piece_win_by_column(self):
        board = IzBoard()
        player = board.current_player()

        # Creates the following board (assuming red goes first):
        #
        # . . . . . . .
        # . . . . . . .
        # R . . . . . .
        # R Y . . . . .
        # R Y . . . . .
        # R Y . . . . .


        board.insert_piece(0)
        board.insert_piece(1)
        board.insert_piece(0)
        board.insert_piece(1)
        board.insert_piece(0)
        board.insert_piece(1)
        board.insert_piece(0)

        self.assertTrue(board.is_gameover())
        self.assertEqual(board.get_winner(), player)

    def test_insert_piece_win_by_row(self):
        board = IzBoard()
        player = board.current_player()

        # Creates the following board (assuming red goes first):
        #
        # . . . . . . .
        # . . . . . . .
        # . . . . . . .
        # . . . . . . .
        # Y Y Y . . . .
        # R R R R . . .

        board.insert_piece(0)
        board.insert_piece(0)
        board.insert_piece(1)
        board.insert_piece(1)
        board.insert_piece(2)
        board.insert_piece(2)
        board.insert_piece(3)

        self.assertTrue(board.is_gameover())
        self.assertEqual(board.get_winner(), player)

    def test_insert_piece_win_by_upward_diagonal(self):
        board = IzBoard()
        player = board.current_player()

        # Creates the following board (assuming red goes first):
        #
        # . . . . . . .
        # . . . . . . .
        # . . . . . . .
        # . . . R . . .
        # . . R Y . . .
        # . R Y R . . .
        # R Y R Y . . Y

        board.insert_piece(0) # R
        board.insert_piece(1) # Y
        board.insert_piece(2) # R
        board.insert_piece(3) # Y

        board.insert_piece(1) # R
        board.insert_piece(2) # Y
        board.insert_piece(3) # R

        # Extra piece needed so that the next piece is red
        board.insert_piece(6) # Y

        board.insert_piece(2) # R
        board.insert_piece(3) # Y

        board.insert_piece(3) # R

        self.assertTrue(board.is_gameover())
        self.assertEqual(board.get_winner(), player)

    def test_insert_piece_win_by_downward_diagonal(self):
        board = IzBoard()
        player = board.current_player()

        # Creates the following board (assuming red goes first):
        #
        # . . . . . . .
        # . . . . . . .
        # . . . . . . .
        # R . . . . . .
        # Y R . . . . .
        # R Y R . . . .
        # Y R Y R . . Y

        board.insert_piece(3) # R
        board.insert_piece(2) # Y
        board.insert_piece(1) # R
        board.insert_piece(0) # Y

        board.insert_piece(2) # R
        board.insert_piece(1) # Y
        board.insert_piece(0) # R

        # Extra piece needed so that the next piece is red
        board.insert_piece(6) # Y

        board.insert_piece(1) # R
        board.insert_piece(0) # Y

        board.insert_piece(1) # R

        self.assertTrue(board.is_gameover())
        self.assertEqual(board.get_winner(), player)

    def test_insert_piece_game_over_no_valid_moves(self):
        board = IzBoard()

        # Creates the following board (assuming red goes first):
        #
        # Y R Y R Y R Y
        # Y R Y R Y R R
        # Y R Y R Y R Y
        # R Y R Y R Y R
        # R Y R Y R Y Y
        # R Y R Y R Y R

        for row in range(6):
            for col in range(6):
                board.insert_piece(col)
        for row in range(6):
            board.insert_piece(6)

        self.assertTrue(board.is_gameover())
        self.assertEqual(board.get_winner(), None)


def other_player(player):
    return Piece.RED if player == Piece.YELLOW else Piece.YELLOW

if __name__ == '__main__':
    unittest.main()