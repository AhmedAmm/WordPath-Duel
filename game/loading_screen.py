import pygame
from settings import *

def draw_loading_screen(screen):
    screen.fill(COLORS['background'])
    title_text = FONT.render("Word-Path Duel", True, COLORS['text'])
    screen.blit(title_text, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 - 150))
    
    pvp_text = FONT.render("Player vs Player", True, COLORS['text'])
    pvp_button = pygame.Rect(WINDOW_WIDTH // 2 - 120, WINDOW_HEIGHT // 2 - 50, 240, 40)
    pygame.draw.rect(screen, COLORS['player'], pvp_button)
    screen.blit(pvp_text, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 - 50))
    
    pvai_text = FONT.render("Player vs AI", True, COLORS['text'])
    pvai_button = pygame.Rect(WINDOW_WIDTH // 2 - 120, WINDOW_HEIGHT // 2, 240, 40)
    pygame.draw.rect(screen, COLORS['ai'], pvai_button)
    screen.blit(pvai_text, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2))
    
    pygame.display.flip()
    return pvp_button, pvai_button