import pygame
from settings import *

def draw_difficulty_screen(screen, current_level):
    screen.fill(COLORS['background'])
    
    # Title
    title_text = FONT.render("Select Difficulty Level", True, COLORS['text'])
    title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 200))
    screen.blit(title_text, title_rect)
    
    # Define parameters for level buttons.
    num_levels = 5
    button_radius = 15
    interval = 75
    # Center the row of buttons horizontally:
    start_x = WINDOW_WIDTH // 2 - ((num_levels - 1) * interval) // 2
    
    # Draw level buttons (circles) and save their collision rects.
    level_buttons = []
    for i in range(num_levels):
        level = i + 1
        center_x = start_x + i * interval
        center_y = WINDOW_HEIGHT // 2
        button_rect = pygame.Rect(center_x - button_radius, center_y - button_radius, button_radius * 2, button_radius * 2)
        level_buttons.append((level, button_rect))
        
        # Draw a filled circle for the selected level; otherwise, an outlined circle.
        if current_level == level:
            pygame.draw.circle(screen, COLORS['player'], (center_x, center_y), button_radius)
        else:
            pygame.draw.circle(screen, COLORS['text'], (center_x, center_y), button_radius, 2)
        
        # Draw the level number on the circle.
        level_text = FONT.render(str(level), True, COLORS['text'])
        text_rect = level_text.get_rect(center=(center_x, center_y))
        screen.blit(level_text, text_rect)
    
    # Display grid size text below the buttons.
    grid_size_value = get_grid_size(current_level)
    grid_size_text = FONT.render(f"Grid Size: {grid_size_value}x{grid_size_value}", True, COLORS['text'])
    grid_size_rect = grid_size_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 40))
    screen.blit(grid_size_text, grid_size_rect)
    
    # Draw "Go Back" button at the top-left.
    go_back_text = FONT.render("Go Back", True, COLORS['text'])
    go_back_button = pygame.Rect(20, 20, 130, 40)
    pygame.draw.rect(screen, COLORS['cell'], go_back_button)
    pygame.draw.rect(screen, COLORS['text'], go_back_button, 2)
    screen.blit(go_back_text, (30, 30))
    
    # Draw "Confirm" button.
    confirm_text = FONT.render("Confirm", True, COLORS['text'])
    confirm_button = pygame.Rect(WINDOW_WIDTH // 2 - 75, WINDOW_HEIGHT // 2 + 80, 150, 40)
    pygame.draw.rect(screen, COLORS['cell'], confirm_button)
    pygame.draw.rect(screen, COLORS['text'], confirm_button, 2)
    confirm_text_rect = confirm_text.get_rect(center=confirm_button.center)
    screen.blit(confirm_text, confirm_text_rect)
    
    pygame.display.flip()
    
    # Return the go-back button, the list of level buttons, and the confirm button.
    return go_back_button, level_buttons, confirm_button

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
