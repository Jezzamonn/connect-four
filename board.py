from enum import Enum

class Piece(Enum):
    EMPTY = 0
    RED = 1
    YELLOW = 2

num_rows = 6
num_cols = 7

class BoardInterface:
    """Interface for a connect four board."""

    def current_player(self):
        """Returns which player gets to make the next move."""
        pass

    def is_gameover(self):
        """Returns True if the game is over, False otherwise."""
        pass

    def get_winner(self):
        """Returns the winner of the game, or None if there is no winner."""
        pass

    def get_piece(self, x, y):
        """Returns the piece at the given location."""
        pass

    def insert_piece(x):
        """Inserts a piece into the given column.

        After this, the current piece will be switched to the other player.

        If the move is invalid, that player immediately loses."""
        pass


class ReadOnlyBoard:
    """A read-only wrapper around a Board, given to players so they can't cheat by using methods they shouldn't.

    You don't need to modify this, it's already complete. :)"""

    def __init__(self, board):
        self._board = board

    def get_piece(self, x, y):
        return self._board.get_piece(x, y)
