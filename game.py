import pygame
from jezimpl.jezboard import JezBoard
from jezimpl.jezaiplayer import JezAIPlayer1, JezAIPlayer2
from board import Piece, num_cols, num_rows
import random


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player1_piece = Piece.RED
player2_piece = Piece.YELLOW
player_classes = [JezAIPlayer1, JezAIPlayer2]

def create_new_game():
    global board, player1, player2, next_player
    # TODO: Replace the board with the real implementation.
    board = JezBoard()

    player1_class = random.choice(player_classes)
    player1 = player1_class(player1_piece)

    player2_class = random.choice(player_classes)
    player2 = player2_class(player2_piece)

    next_player = player1

create_new_game()

background_color = '#ffffff'
frame_color = '#3b35e8'
text_color = frame_color
red_piece_color = '#e62727'
yellow_piece_color = '#ffc800'

time_until_next_turn = 0

def simulate_turn():
    if board.is_gameover():
        create_new_game()
        return

    global next_player
    next_move = next_player.get_next_move(board)
    board.insert_piece(next_move)
    if next_player == player1:
        next_player = player2
    else:
        next_player = player1

def draw_board(board):
    piece_size = 80
    piece_spacing = 20
    pieces_width = num_cols * (piece_size + piece_spacing) + piece_spacing;
    pieces_height = num_rows * (piece_size + piece_spacing) + piece_spacing;

    # Aligned to the hortizontal center of the screen.
    pieces_x_start = (screen.get_width() - pieces_width) // 2
    # Aligned to the bottom of the screen.
    pieces_y_start = screen.get_height() - pieces_height;

    screen.fill(background_color)

    # Draw the frame as a rounded rectangle.
    pygame.draw.rect(
        screen,
        frame_color,
        pygame.Rect(
            pieces_x_start,
            pieces_y_start,
            pieces_width,
            pieces_height
        ),
        border_radius=20
    )

    # Draw the pieces.
    for x in range(num_cols):
        for y in range(num_rows):
            piece = board.get_piece(x, y)
            if piece == Piece.EMPTY:
                color = background_color
            elif piece == Piece.RED:
                color = red_piece_color
            elif piece == Piece.YELLOW:
                color = yellow_piece_color
            else:
                raise ValueError(f"Unknown piece {piece}")

            circle_x = pieces_x_start + x * (piece_size + piece_spacing) + piece_spacing + piece_size // 2
            circle_y = pieces_y_start + y * (piece_size + piece_spacing) + piece_spacing + piece_size // 2

            pygame.draw.circle(
                screen,
                color,
                (circle_x, circle_y),
                piece_size // 2
            )

    # Say which player is next or which player is winning
    if board.is_gameover():
        winner = board.get_winner()
        if winner == Piece.RED:
            text = "Red wins!"
        elif winner == Piece.YELLOW:
            text = "Yellow wins!"
        else:
            text = "It's a tie!"
    else:
        player_piece = player1_piece if next_player == player1 else player2_piece
        # Class name of the player
        player_name = next_player.__class__.__name__
        text = f"Next player: {player_piece.name} ({player_name})"

    font = pygame.font.SysFont('Arial', 30)
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, (0, 0))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if time_until_next_turn <= 0:
        simulate_turn()
        draw_board(board)
        if board.is_gameover():
            time_until_next_turn = 3
        else:
            time_until_next_turn = 0.5


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)
    time_until_next_turn -= 1 / 60


pygame.quit()