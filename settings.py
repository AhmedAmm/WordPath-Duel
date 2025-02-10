import pygame 
from algorithms.minimax import Minimax

pygame.init()

# Window configurations
PADDING = 30
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT
FPS = 60

# Game configurations
ROWS = 10
COLUMNS = 10
CELL_SIZE = 30

# Colors
COLORS = {
    'background': (240, 240, 240),
    'cell': (255, 255, 255),
    'player': (0, 200, 0),
    'ai': (200, 0, 0),
    'text': (0, 0, 0)
}
GRAY = "#1C1C1C"

# Font config
FONT = pygame.font.Font(None, 36)
SMALL_FONT = pygame.font.Font(None, 24)

WORDS = [("a", 5), ("ab", 3), ("abc", -2), ("abcd", 2), ("abcde", -1), ("aab", 1)]
