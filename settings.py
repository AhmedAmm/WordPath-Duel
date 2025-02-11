import pygame 
from algorithms.minimax import Minimax

pygame.init()

# Window configurations
PADDING = 30
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT
FPS = 60
UI_WIDTH = 200

# Game configurations
ROWS = 10
COLUMNS = 10
CELL_SIZE = 30

# Colors
HIGHLIGHT_COLOR = (255, 255, 0)
COLORS = {
    'background': (28, 28, 28),  # Dark background
    'cell': (70, 70, 70),        # Slightly lighter for grid cells
    'player': (0, 200, 0),       # Bright green for the player
    'ai': (200, 0, 0),           # A vivid red for the AI
    'text': (255, 255, 255)      # White text for contrast
}
GRAY = "#1C1C1C"

# Font config
FONT = pygame.font.Font(None, 36)
SMALL_FONT = pygame.font.Font(None, 24)

WORDS = [("a", 5), ("ab", 3), ("abc", -2), ("abcd", 2), ("abcde", -1), ("aab", 1)]
