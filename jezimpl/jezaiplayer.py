from board import num_cols
from aiplayer import AIPlayer
import random

class JezAIPlayerRandom(AIPlayer):

    def get_next_move(self, board):
        return random.randint(0, num_cols)

class JezAIPlayerFirstCol(AIPlayer):

    def get_next_move(self, board):
        return 0

class JezAIPlayerInvalid(AIPlayer):

    def get_next_move(self, board):
        return 10
