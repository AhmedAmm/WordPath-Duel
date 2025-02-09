import pygame

def draw_player_selection_screen(screen, COLORS, FONT, WIDTH, HEIGHT, duck_1, duck_2, selected_duck):
    screen.fill(COLORS['background'])
    title_text = FONT.render("Select Your Player", True, COLORS['text'])
    screen.blit(title_text, (WIDTH // 2 - 150, HEIGHT // 2 - 200))
    
    # Resize images
    duck_1 = pygame.transform.scale(duck_1, (200, 200))
    duck_2 = pygame.transform.scale(duck_2, (200, 200))
    
    # Define image positions
    duck_1_pos = (WIDTH // 2 - 250, HEIGHT // 2 - 100)
    duck_2_pos = (WIDTH // 2 + 50, HEIGHT // 2 - 100)
    
    # Draw borders
    if selected_duck == "duck_1":
        pygame.draw.rect(screen, COLORS['player'], (*duck_1_pos, 200, 200), 5)
    else:
        pygame.draw.rect(screen, COLORS['cell'], (*duck_1_pos, 200, 200), 5)
    
    if selected_duck == "duck_2":
        pygame.draw.rect(screen, COLORS['player'], (*duck_2_pos, 200, 200), 5)
    else:
        pygame.draw.rect(screen, COLORS['cell'], (*duck_2_pos, 200, 200), 5)
    
    # Draw images
    screen.blit(duck_1, duck_1_pos)
    screen.blit(duck_2, duck_2_pos)
    
    # Draw confirm button
    confirm_text = FONT.render("Confirm", True, COLORS['text'])
    confirm_button = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 + 150, 150, 40)
    pygame.draw.rect(screen, COLORS['cell'], confirm_button)
    pygame.draw.rect(screen, COLORS['text'], confirm_button, 2)
    screen.blit(confirm_text, (confirm_button.centerx - confirm_text.get_width() // 2, confirm_button.centery - confirm_text.get_height() // 2))
    
    pygame.display.flip()
    return duck_1_pos, duck_2_pos, confirm_button