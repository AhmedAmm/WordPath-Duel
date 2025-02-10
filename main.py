from settings import *
import pygame
import sys
from game.loading_screen import draw_loading_screen
from game.difficulty_screen import draw_difficulty_screen, get_grid_size
from game.grid import create_grid, draw_grid
from game.ui import draw_ui
from game.player_selection_screen import draw_player_selection_screen
from game.game_logic import handle_player_turn, ai_turn

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Word-Path Duel")

        self.running = True
        self.game_mode = None
        self.difficulty_level = None
        self.grid_size = 5  # Default grid size
        self.grid = None
        self.player_choice = None
        self.player_image = None
        self.ai_image = None
        self.selected_cells = []
        self.current_word = ""
        self.player_turn = True
        self.message = ""
        self.valid_words_found = set()
        self.overall_score = 0

        self.minimax = None
        
        # UI Elements
        self.pvp_button = None
        self.pvai_button = None
        self.go_back_button = None
        self.slider_rect = None
        self.confirm_button = None
        self.duck_1_pos = None
        self.duck_2_pos = None

        # Load images
        try:
            self.duck_1 = pygame.image.load('images/duck_1.png')
            self.duck_1 = pygame.transform.scale(self.duck_1, (40, 40))
        except pygame.error as e:
            print(f"Error loading duck_1: {e}")
            sys.exit()

        try:
            self.duck_2 = pygame.image.load('images/duck_2.png')
            self.duck_2 = pygame.transform.scale(self.duck_2, (40, 40))
        except pygame.error as e:
            print(f"Error loading duck_2: {e}")
            sys.exit()

    def run(self):
        while self.running:
            self.screen.fill(GRAY)
            
            if self.game_mode is None:
                self.pvp_button, self.pvai_button = draw_loading_screen(self.screen, COLORS, FONT, 1280, 720)
                self.handle_menu_events()
            elif self.game_mode == "PVA" and self.grid is None:
                self.go_back_button, self.slider_rect, self.confirm_button = draw_difficulty_screen(self.screen, self.difficulty_level or 1)
                self.handle_difficulty_selection()
            elif self.game_mode == "PVA" and self.player_choice is None:
                self.duck_1_pos, self.duck_2_pos, self.confirm_button = draw_player_selection_screen(self.screen, self.duck_1, self.duck_2, self.player_choice)
                self.handle_player_selection()
            else:
                self.handle_gameplay()
            
            pygame.display.flip()
            self.clock.tick(FPS)

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.pvp_button and self.pvp_button.collidepoint(event.pos):
                    self.game_mode = "PVP"
                    self.difficulty_level = 1
                    self.grid_size = get_grid_size(self.difficulty_level)
                    self.minimax = create_grid(self.grid_size, WORDS)
                    self.grid = self.minimax.grid_gen()
                elif self.pvai_button and self.pvai_button.collidepoint(event.pos):
                    self.game_mode = "PVA"
                    self.difficulty_level = None
    
    def handle_difficulty_selection(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.go_back_button and self.go_back_button.collidepoint(event.pos):
                    self.game_mode = None
                elif self.slider_rect and self.slider_rect.collidepoint(event.pos):
                    self.difficulty_level = (event.pos[0] - (1280 // 2 - 150)) // 75 + 1
                    self.difficulty_level = max(1, min(self.difficulty_level, 5))
                elif self.confirm_button and self.confirm_button.collidepoint(event.pos) and self.difficulty_level:
                    self.grid_size = get_grid_size(self.difficulty_level)
                    self.minimax = create_grid(self.grid_size, WORDS)
                    self.grid = self.minimax.grid_gen()
                    self.player_choice = None
    
    def handle_player_selection(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.duck_1_pos and self.duck_1_pos[0] <= event.pos[0] <= self.duck_1_pos[0] + 200:
                    self.player_choice = "duck_1"
                    self.player_image = self.duck_1
                    self.ai_image = self.duck_2
                elif self.duck_2_pos and self.duck_2_pos[0] <= event.pos[0] <= self.duck_2_pos[0] + 200:
                    self.player_choice = "duck_2"
                    self.player_image = self.duck_2
                    self.ai_image = self.duck_1
                elif self.confirm_button and self.confirm_button.collidepoint(event.pos) and self.player_choice:
                    pass
    
    def handle_gameplay(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and self.player_turn:
                self.player_turn, self.selected_cells, self.current_word, self.message, self.overall_score = handle_player_turn(self.grid, self.grid_size, self.selected_cells, self.current_word, self.player_turn, self.message, self.overall_score, self.minimax)
        
        if self.game_mode == "PVA" and not self.player_turn:
            self.player_turn, self.selected_cells, self.current_word, self.message, self.overall_score = ai_turn(
                self.grid, self.grid_size, self.selected_cells, self.current_word, self.player_turn, 
                self.message, self.overall_score, self.minimax
            )

        draw_grid(self.screen, self.grid, self.selected_cells, self.player_turn, COLORS, FONT, SMALL_FONT, 1280, 720, self.grid_size, self.player_image, self.ai_image)
        self.go_back_button = draw_ui(self.screen, self.overall_score, self.current_word, self.message, self.valid_words_found, COLORS, FONT, SMALL_FONT, 1280, 720)

if __name__ == "__main__":
    main = Main()
    main.run()
