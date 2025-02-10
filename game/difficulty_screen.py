import pygame
from settings import *

def draw_difficulty_screen(screen, level):
    screen.fill(COLORS['background'])
    title_text = FONT.render("Select Difficulty Level", True, COLORS['text'])
    screen.blit(title_text, (WINDOW_WIDTH // 2 - 150, WINDOW_HEIGHT // 2 - 200))
    
    slider_rect = pygame.Rect(WINDOW_WIDTH // 2 - 150, WINDOW_HEIGHT // 2 - 50, 300, 10)
    pygame.draw.rect(screen, COLORS['text'], slider_rect)
    
    for i in range(1, 6):
        level_pos = WINDOW_WIDTH // 2 - 150 + (i - 1) * 75
        pygame.draw.circle(screen, COLORS['text'], (level_pos, WINDOW_HEIGHT // 2 - 45), 10)
        level_text = FONT.render(f"{i}", True, COLORS['text'])
        screen.blit(level_text, (level_pos - 10, WINDOW_HEIGHT // 2 - 80))
    
    handle_pos = WINDOW_WIDTH // 2 - 150 + (level - 1) * 75
    pygame.draw.circle(screen, COLORS['player'], (handle_pos,WINDOW_HEIGHT // 2 - 45), 15)
    
    grid_size_text = FONT.render(f"Grid Size: {get_grid_size(level)}x{get_grid_size(level)}", True, COLORS['text'])
    screen.blit(grid_size_text, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 + 20))
    
    go_back_text = FONT.render("Go Back", True, COLORS['text'])
    go_back_button = pygame.Rect(20, 20, 130, 40)
    pygame.draw.rect(screen, COLORS['cell'], go_back_button)
    pygame.draw.rect(screen, COLORS['text'], go_back_button, 2)
    screen.blit(go_back_text, (30, 30))
    
    confirm_text = FONT.render("Confirm", True, COLORS['text'])
    confirm_button = pygame.Rect(WINDOW_WIDTH // 2 - 75, WINDOW_HEIGHT // 2 + 80, 150, 40)
    pygame.draw.rect(screen, COLORS['cell'], confirm_button)
    pygame.draw.rect(screen, COLORS['text'], confirm_button, 2)
    screen.blit(confirm_text, (confirm_button.centerx - confirm_text.get_width() // 2, confirm_button.centery - confirm_text.get_height() // 2))
    
    pygame.display.flip()
    return go_back_button, slider_rect, confirm_button

def get_grid_size(level):
    if level == 1:
        return 5
    elif level == 2:
        return 7
    elif level == 3:
        return 10
    elif level == 4:
        return 12
    elif level == 5:
        return 15