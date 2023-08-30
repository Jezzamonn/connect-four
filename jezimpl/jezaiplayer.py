from board import num_cols
from aiplayer import AIPlayer
import random

class JezAIPlayer(AIPlayer):

    def get_next_move(self, board):
        return random.randint(0, num_cols)