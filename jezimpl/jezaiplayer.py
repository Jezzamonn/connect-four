from board import num_cols
from aiplayer import AIPlayerInterface
import random

class JezAIPlayerRandom(AIPlayerInterface):

    def get_next_move(self, board):
        return random.randint(0, num_cols)

class JezAIPlayerFirstCol(AIPlayerInterface):

    def get_next_move(self, board):
        return 0

class JezAIPlayerInvalid(AIPlayerInterface):

    def get_next_move(self, board):
        return 10
