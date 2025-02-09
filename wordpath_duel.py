import pygame
import random
import sys
from algorithms.minimax import Minimax
from game.loading_screen import draw_loading_screen
from game.difficulty_screen import draw_difficulty_screen, get_grid_size
from game.grid import create_grid, draw_grid
from game.ui import draw_ui
from game.player_selection_screen import draw_player_selection_screen
from utils.utils import check_word
from game.game_logic import handle_player_turn, ai_turn
from utils.word_generator import generate_words

pygame.init()
pygame.display.init()

COLORS = {
    'background': (240, 240, 240),
    'cell': (255, 255, 255),
    'player': (0, 200, 0),
    'ai': (200, 0, 0),
    'text': (0, 0, 0)
}

FONT = pygame.font.Font(None, 36)
SMALL_FONT = pygame.font.Font(None, 24)

# Load images
duck_1 = pygame.image.load('images/duck_1.png')
duck_2 = pygame.image.load('images/duck_2.png')

# Resize images to fit inside the grid cell
duck_1 = pygame.transform.scale(duck_1, (40, 40))
duck_2 = pygame.transform.scale(duck_2, (40, 40))

# Letter score
LETTER_VALUES = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2,
    'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1,
    'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
    'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

# Dict
WORD_LIST = split.generate_words()

overall_score = 0
selected_cells = []
current_word = ""
player_turn = True
message = ""
valid_words_found = set()
game_mode = None
difficulty_level = None  # Set to None initially
grid_size = 5  # Default grid size
grid = None  # Grid will be created once difficulty is chosen
player_choice = None  # Player choice will be set after selection
player_image = None  # Player image will be set after selection
ai_image = None  # AI image will be set after selection

# display
WIDTH, HEIGHT = 800, 600  # Set fixed window size
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Word-Path Duel")

# Main
running = True
pvp_button = None
pvai_button = None
go_back_button = None
slider_rect = None
confirm_button = None
duck_1_pos = None
duck_2_pos = None

while running:
    if game_mode is None:
        pvp_button, pvai_button = draw_loading_screen(screen, COLORS, FONT, WIDTH, HEIGHT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pvp_button.collidepoint(event.pos):
                    game_mode = "PVP"
                    difficulty_level = 1
                    grid_size = get_grid_size(difficulty_level)
                    grid = create_grid(grid_size, LETTER_VALUES)
                elif pvai_button.collidepoint(event.pos):
                    game_mode = "PVA"
                    difficulty_level = None  # Reset difficulty level
    elif game_mode == "PVA" and grid is None:
        go_back_button, slider_rect, confirm_button = draw_difficulty_screen(screen, COLORS, FONT, WIDTH, HEIGHT, difficulty_level or 1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if go_back_button.collidepoint(event.pos):
                    game_mode = None
                elif slider_rect.collidepoint(event.pos):
                    difficulty_level = (event.pos[0] - (WIDTH // 2 - 150)) // 75 + 1
                    difficulty_level = max(1, min(difficulty_level, 5))
                    go_back_button, slider_rect, confirm_button = draw_difficulty_screen(screen, COLORS, FONT, WIDTH, HEIGHT, difficulty_level)
                elif confirm_button.collidepoint(event.pos):
                    if difficulty_level:
                        grid_size = get_grid_size(difficulty_level)
                        grid = create_grid(grid_size, LETTER_VALUES)
                        player_choice = None  # Reset player choice
    elif game_mode == "PVA" and player_choice is None:
        duck_1_pos, duck_2_pos, confirm_button = draw_player_selection_screen(screen, COLORS, FONT, WIDTH, HEIGHT, duck_1, duck_2, player_choice)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if duck_1_pos[0] <= event.pos[0] <= duck_1_pos[0] + 200 and duck_1_pos[1] <= event.pos[1] <= duck_1_pos[1] + 200:
                    player_choice = "duck_1"
                    player_image = duck_1
                    ai_image = duck_2
                elif duck_2_pos[0] <= event.pos[0] <= duck_2_pos[0] + 200 and duck_2_pos[1] <= event.pos[1] <= duck_2_pos[1] + 200:
                    player_choice = "duck_2"
                    player_image = duck_2
                    ai_image = duck_1
                elif confirm_button.collidepoint(event.pos) and player_choice:
                    # Proceed to the game
                    grid = create_grid(grid_size, LETTER_VALUES)
    else:
        screen.fill(COLORS['background'])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN and player_turn:
                player_turn, selected_cells, current_word, message = handle_player_turn(event, grid, grid_size, selected_cells, current_word, player_turn, message, overall_score, valid_words_found, WORD_LIST)
                        
        if game_mode == "PVA" and not player_turn:
            player_turn, selected_cells, current_word, message = ai_turn(grid, grid_size, selected_cells, current_word, player_turn, message, overall_score, valid_words_found, WORD_LIST)
        
        draw_grid(screen, grid, selected_cells, player_turn, COLORS, FONT, SMALL_FONT, WIDTH, HEIGHT, grid_size, player_image, ai_image)
        go_back_button = draw_ui(screen, overall_score, current_word, message, valid_words_found, COLORS, FONT, SMALL_FONT, WIDTH, HEIGHT)
        pygame.display.flip()

pygame.quit()
sys.exit()