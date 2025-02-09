import pygame
import random

def create_grid(grid_size, LETTER_VALUES):
    grid = []
    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            letter = chr(random.randint(ord('A'), ord('Z')))
            row.append({
                'letter': letter,
                'score': LETTER_VALUES.get(letter, 0),
            })
        grid.append(row)
    return grid

def draw_grid(screen, grid, selected_cells, player_turn, COLORS, FONT, SMALL_FONT, WIDTH, HEIGHT, grid_size, player_image, ai_image):
    cell_size = min(WIDTH // grid_size, HEIGHT // grid_size)
    for i in range(grid_size):
        for j in range(grid_size):
            cell = grid[i][j]
            x = j * cell_size
            y = i * cell_size
        
            if (i, j) in selected_cells:
                color = COLORS['player'] if player_turn else COLORS['ai']
            else:
                color = COLORS['cell']
                
            pygame.draw.rect(screen, color, (x, y, cell_size, cell_size))
            pygame.draw.rect(screen, COLORS['text'], (x, y, cell_size, cell_size), 1)
            
            text = FONT.render(cell['letter'], True, COLORS['text'])
            screen.blit(text, (x + cell_size // 4, y + cell_size // 4))
            
            score_text = SMALL_FONT.render(str(cell['score']), True, COLORS['text'])
            screen.blit(score_text, (x + 3 * cell_size // 4, y + 3 * cell_size // 4))
    
    # Draw player and AI images in the top-left cell
    if player_image:
        screen.blit(player_image, (0, 0))
    if ai_image:
        screen.blit(ai_image, (cell_size - ai_image.get_width(), cell_size - ai_image.get_height()))