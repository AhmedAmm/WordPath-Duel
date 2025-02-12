from settings import *
import pygame
from game.loading_screen import draw_loading_screen
from game.difficulty_screen import draw_difficulty_screen, get_grid_size
from game.grid import create_grid, draw_grid
from game.ui import draw_ui
from game.game_logic import handle_player_turn, ai_turn
from utils.word_generator import generate_words
from algorithms.trie import Trie
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'  # Optional: Set window position
os.environ['SDL_VIDEO_CENTERED'] = '1'  # Center the window
os.environ['SDL_VIDEODRIVER'] = 'directx'  # Use DirectX for hardware acceleration (Windows)

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Word-Path Duel")

        self.running = True
        self.game_mode = None
        self.difficulty_level = None
        self.grid_size = 5  # Default grid size
        self.grid = None
        self.player_choice = None
        self.selected_cells = []
        self.current_word = ""
        self.player_turn = True
        self.message = ""
        self.overall_score = 0
        self.minimax = None

        self.words = generate_words(6)

        self.trie = Trie(1, 1)
        self.init_trie()

        # UI Elements
        self.pvp_button = None
        self.pvai_button = None
        self.go_back_button = None
        self.slider_rect = None
        self.confirm_button = None

    def init_trie(self):
        for word, score in self.words:
            self.trie.insert(word[::-1], score)

    def run(self):
        while self.running:
            self.screen.fill(GRAY)

            if self.game_mode is None:
                self.pvp_button, self.pvai_button = draw_loading_screen(self.screen)
                self.handle_menu_events()
            elif self.game_mode == "PVA" and self.grid is None:
                self.go_back_button, self.slider_rect, self.confirm_button = draw_difficulty_screen(self.screen, self.difficulty_level or 1)
                self.handle_difficulty_selection()
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
                    self.minimax = create_grid(self.grid_size, self.words)
                    self.grid = self.minimax.grid_gen()
                    self.selected_cells = [(0, 0)]
                    self.current_word = self.grid[0][0]
                elif self.pvai_button and self.pvai_button.collidepoint(event.pos):
                    self.game_mode = "PVA"
                    self.difficulty_level = 1

    def handle_difficulty_selection(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.go_back_button and self.go_back_button.collidepoint(event.pos):
                    self.game_mode = None
                else:
                    # Loop over the level buttons (returned as a list of (level, rect) tuples)
                    clicked_level = None
                    for level, btn_rect in self.slider_rect:
                        if btn_rect.collidepoint(event.pos):
                            clicked_level = level
                            break
                    if clicked_level:
                        self.difficulty_level = clicked_level

                    # If the Confirm button is clicked and a level is selected, update grid.
                    if self.confirm_button and self.confirm_button.collidepoint(event.pos) and self.difficulty_level:
                        self.grid_size = get_grid_size(self.difficulty_level)
                        self.minimax = create_grid(self.grid_size, self.words)
                        self.grid = self.minimax.grid_gen()
                        self.player_choice = None
                        self.selected_cells = [(0, 0)]
                        self.current_word = self.grid[0][0]
                        self.player_turn = True
                        self.overall_score = self.trie.work(self.current_word)

    def handle_gameplay(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the "Go Back" button was clicked.
                if self.go_back_button and self.go_back_button.collidepoint(event.pos):
                    # Reset grid (and related state) so that we return to difficulty selection.
                    self.grid = None
                    self.selected_cells = []
                    self.current_word = ""
                    # Optionally, you can also reset other gameplay values:
                    self.overall_score = 0
                    self.message = ""
                    self.game_mode = "PVA"
                    return
                # Otherwise, if it's the player's turn, handle the player's move.
                elif self.player_turn:
                    (self.player_turn,
                     self.selected_cells,
                     self.current_word,
                     self.message,
                     self.overall_score) = handle_player_turn(
                        self.grid, self.grid_size, self.selected_cells, self.current_word,
                        self.player_turn, self.message, self.overall_score, self.trie, self.minimax
                    )

                    # Draw the updated interface after the player's move.
                    draw_grid(self.screen, self.grid, self.selected_cells, self.player_turn, self.grid_size)
                    self.go_back_button = draw_ui(self.screen, self.overall_score, self.current_word, self.message, self.words)
                    pygame.display.flip()  # Update the display to show the changes.

                    # Add a 1-second delay before the AI's turn.
                    pygame.time.delay(1000)  # 1000 milliseconds = 1 second
                    # Alternatively, you can use time.sleep(1)

        # If it's the AI's turn in PVA mode, let the AI move.
        if self.game_mode == "PVA" and not self.player_turn:
            (self.player_turn,
             self.selected_cells,
             self.current_word,
             self.message,
             self.overall_score) = ai_turn(
                self.grid, self.grid_size, self.selected_cells, self.current_word,
                self.player_turn, self.message, self.overall_score, self.minimax, self.trie
            )

        # Draw the updated interface after the AI's move.
        draw_grid(self.screen, self.grid, self.selected_cells, self.player_turn, self.grid_size)
        self.go_back_button = draw_ui(self.screen, self.overall_score, self.current_word, self.message, self.words)
        pygame.display.flip()  # Update the display to show the changes.


if __name__ == "__main__":
    main = Main()
    main.run()
