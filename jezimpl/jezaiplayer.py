from board import num_cols
from aiplayer import AIPlayer
import random

class JezAIPlayer1(AIPlayer):

    def get_next_move(self, board):
        return random.randint(0, num_cols)

class JezAIPlayer2(AIPlayer):

    def get_next_move(self, board):
        return 0