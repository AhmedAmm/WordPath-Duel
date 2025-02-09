import pygame

def draw_ui(screen, overall_score, current_word, message, valid_words_found, COLORS, FONT, SMALL_FONT, WIDTH, HEIGHT):
    text = FONT.render(f"Score: {overall_score}", True, COLORS['player'])
    screen.blit(text, (WIDTH - 200, 20))
    
    word_text = FONT.render(f"Current: {current_word}", True, COLORS['text'])
    screen.blit(word_text, (WIDTH - 200, 60))
    
    msg_text = FONT.render(message, True, COLORS['text'])
    screen.blit(msg_text, (WIDTH - 200, 100))
    
    found_text = SMALL_FONT.render("Found words: " + ", ".join(valid_words_found), 
                                 True, COLORS['text'])
    screen.blit(found_text, (WIDTH - 200, 140))
    
    go_back_text = FONT.render("Go Back", True, COLORS['text'])
    go_back_button = pygame.Rect(WIDTH - 200, HEIGHT - 60, 100, 40)
    pygame.draw.rect(screen, COLORS['cell'], go_back_button)
    pygame.draw.rect(screen, COLORS['text'], go_back_button, 2)
    screen.blit(go_back_text, (WIDTH - 190, HEIGHT - 50))
    
    return go_back_button