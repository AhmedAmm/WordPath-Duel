import pygame
from algorithms.minimax import Minimax
from settings import *

def create_grid(grid_size, words):
    minimax = Minimax(grid_size, grid_size, words)
    return minimax

def draw_grid(screen, grid, selected_cells, player_turn, grid_size):
    # Use the grid drawing area: leave UI_WIDTH on the right.
    grid_area_width = WINDOW_WIDTH - UI_WIDTH  
    cell_width = grid_area_width // grid_size
    cell_height = WINDOW_HEIGHT // grid_size
    
    for i in range(grid_size):
        for j in range(grid_size):
            cell_letter = grid[i][j]  # Each cell is a letter (string)
            x = j * cell_width
            y = i * cell_height
        
            if (i, j) in selected_cells:
                color = COLORS['player'] if player_turn else COLORS['ai']
            else:
                color = COLORS['cell']
                
            pygame.draw.rect(screen, color, (x, y, cell_width, cell_height))
            pygame.draw.rect(screen, COLORS['text'], (x, y, cell_width, cell_height), 1)
            
            # Render the letter centered in the cell
            text = FONT.render(cell_letter.upper(), True, COLORS['text'])  
            text_rect = text.get_rect(center=(x + cell_width // 2, y + cell_height // 2))
            screen.blit(text, text_rect)

    # Highlight valid moves (right and down) if it's the player's turn.
    if selected_cells:
        last_row, last_col = selected_cells[-1]
    else:
        last_row, last_col = (0, 0)

    if player_turn:
        # Highlight the right move if available.
        if last_col + 1 < grid_size and (last_row, last_col + 1) not in selected_cells:
            highlight_x = (last_col + 1) * cell_width
            highlight_y = last_row * cell_height
            pygame.draw.rect(screen, HIGHLIGHT_COLOR, (highlight_x, highlight_y, cell_width, cell_height), 3)
        # Highlight the down move if available.
        if last_row + 1 < grid_size and (last_row + 1, last_col) not in selected_cells:
            highlight_x = last_col * cell_width
            highlight_y = (last_row + 1) * cell_height
            pygame.draw.rect(screen, HIGHLIGHT_COLOR, (highlight_x, highlight_y, cell_width, cell_height), 3)
