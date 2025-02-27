import pygame
from utils.utils import is_valid_selection
from settings import *
import time
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'  # Optional: Set window position
os.environ['SDL_VIDEO_CENTERED'] = '1'  # Center the window
os.environ['SDL_VIDEODRIVER'] = 'directx'  # Use DirectX for hardware acceleration (Windows)


def handle_player_turn(grid, grid_size, selected_cells, current_word, player_turn, message, overall_score, trie_instance, minimax_instance):
    """Handles player's turn by allowing them to move right or down and update their score."""
    
    x, y = pygame.mouse.get_pos()
    row, col = get_grid_coords(x, y, grid_size)

    if 0 <= row < grid_size and 0 <= col < grid_size:
        if selected_cells:
            last_row, last_col = selected_cells[-1]

            # Enforce movement only to the right or down
            if (row == last_row and col == last_col + 1) or (col == last_col and row == last_row + 1):
                if is_valid_selection(selected_cells, row, col):
                    selected_cells.append((row, col))
                    current_word += grid[row][col]  # Extract letter from grid
                    message = ""

                    # Use minimax to evaluate the player's move
                    overall_score += trie_instance.work(current_word[::-1])

                    # If at the bottom-right, end the turn
                    if row == grid_size - 1 and col == grid_size - 1:
                        player_turn = False
                    else:
                        player_turn = False  # AI's turn next
                else:
                    message = "Invalid selection!"
            else:
                message = "Invalid move! You can only move right or down."

    return player_turn, selected_cells, current_word, message, overall_score




def ai_turn(grid, grid_size, selected_cells, current_word, player_turn, message, overall_score, minimax_instance, trie_instance):
    """AI selects the best move using Minimax and updates the game state accordingly."""
    if selected_cells:
        row, col = selected_cells[-1]
    else:
        row, col = 0, 0  # Start position

    # Use minimax to determine best move
    _, best_move = minimax_instance.minimax(row, col, current_word)

    # Make the move (right or down)
    if best_move == 'R' and col + 1 < grid_size:
        col += 1
    elif best_move == 'D' and row + 1 < grid_size:
        row += 1
    else:
        return player_turn, selected_cells, current_word, message, overall_score

    # Update AI path
    selected_cells.append((row, col))
    current_word += grid[row][col]  # Append letter from grid
    overall_score += trie_instance.work(current_word[::-1])

    # If at the bottom-right, end the game
    if row == grid_size - 1 and col == grid_size - 1:
        player_turn = False  # Player's turn next
    else:
        player_turn = True

    return player_turn, selected_cells, current_word, message, overall_score

def get_grid_coords(x, y, grid_size):
    grid_area_width = WINDOW_WIDTH - UI_WIDTH
    col = x // (grid_area_width // grid_size)
    row = y // (WINDOW_HEIGHT // grid_size)
    return row, col
