from board import Board, Piece
import random

class JezBoard(Board):

    def __init__(self):
        self.winner = None

    def current_player(self):
        return Piece.RED;

    def is_gameover(self):
        return self.winner is not None

    def get_winner(self):
        return self.winner

    def get_piece(self, x, y):
        return random.choice([Piece.RED, Piece.YELLOW, Piece.EMPTY])

    def insert_piece(self, x):
        # A random chance of saying the game is over
        if random.random() < (1 / 20):
            self.winner = Piece.RED


