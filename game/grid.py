import pygame
from algorithms.minimax import Minimax

def create_grid(grid_size, words):
    minimax = Minimax(grid_size, grid_size, words)
    return minimax

def draw_grid(screen, grid, selected_cells, player_turn, COLORS, FONT, SMALL_FONT, WIDTH, HEIGHT, grid_size, player_image, ai_image):
    cell_size = min(WIDTH // grid_size, HEIGHT // grid_size)
    
    for i in range(grid_size):
        for j in range(grid_size):
            cell_letter = grid[i][j]  # Now, each cell is just a letter (string)
            x = j * cell_size
            y = i * cell_size
        
            if (i, j) in selected_cells:
                color = COLORS['player'] if player_turn else COLORS['ai']
            else:
                color = COLORS['cell']
                
            pygame.draw.rect(screen, color, (x, y, cell_size, cell_size))
            pygame.draw.rect(screen, COLORS['text'], (x, y, cell_size, cell_size), 1)
            
            # Render the letter in the center of the cell
            text = FONT.render(cell_letter.upper(), True, COLORS['text'])  
            text_rect = text.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
            screen.blit(text, text_rect)
    
    # Draw player and AI images in the top-left cell
    if player_image:
        screen.blit(player_image, (0, 0))
    if ai_image:
        screen.blit(ai_image, (cell_size - ai_image.get_width(), cell_size - ai_image.get_height()))
