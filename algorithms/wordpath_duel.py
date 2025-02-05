import pygame
import random
import sys
from minimax import Minimax
from loading_screen import draw_loading_screen
from difficulty_screen import draw_difficulty_screen, get_grid_size

pygame.init()
pygame.display.init()

COLORS = {
    'background': (240, 240, 240),
    'cell': (255, 255, 255),
    'player': (0, 200, 0),
    'ai': (200, 0, 0),
    'text': (0, 0, 0)
}

FONT = pygame.font.Font(None, 36)
SMALL_FONT = pygame.font.Font(None, 24)

# Letter score
LETTER_VALUES = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2,
    'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1,
    'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
    'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

# Dict
WORD_LIST = ["PYGAME", "PYTHON", "PROGRAM", "MATRIX", 
            "SCORE", "PLAYER", "COMPUTER", "WORD", "INTELLIGENCE", "ARTIFICIAL"]

def create_grid(grid_size):
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

overall_score = 0
selected_cells = []
current_word = ""
player_turn = True
message = ""
valid_words_found = set()
game_mode = None
difficulty_level = None  # Set to None initially
grid_size = 5  # Default grid size
grid = None  # Grid will be created once difficulty is chosen

# display
WIDTH, HEIGHT = 800, 600  # Set fixed window size
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Word-Path Duel")

def draw_grid():
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

def draw_ui():
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

def check_word():
    global overall_score, valid_words_found, message
    word = current_word.upper()
    
    if word in WORD_LIST and word not in valid_words_found:
        score = sum(grid[r][c]['score'] for r, c in selected_cells)
        overall_score += score
        valid_words_found.add(word)
        message = f"Found {word}! +{score} points"
        return True
    return False

def is_valid_selection(new_row, new_col):
    if not selected_cells:
        return new_row == 0 and new_col == 0  #(0,0)
    
    last_row, last_col = selected_cells[-1]
    return abs(new_row - last_row) + abs(new_col - last_col) == 1

def ai_turn():
    global player_turn, selected_cells, current_word, message
    minimax = Minimax(grid_size, grid_size)
    minimax.grid = [[grid[i][j]['letter'] for j in range(grid_size)] for i in range(grid_size)]
    score, move = minimax.minimax(0, 0, "")
    if move == 'D':
        selected_cells.append((selected_cells[-1][0] + 1, selected_cells[-1][1]))
    elif move == 'R':
        selected_cells.append((selected_cells[-1][0], selected_cells[-1][1] + 1))
    current_word += grid[selected_cells[-1][0]][selected_cells[-1][1]]['letter']
    if check_word():
        selected_cells = []
        current_word = ""
    player_turn = True

# Main
running = True
pvp_button = None
pvai_button = None
go_back_button = None
slider_rect = None
confirm_button = None

while running:
    if game_mode is None:
        pvp_button, pvai_button = draw_loading_screen(screen, COLORS, FONT, WIDTH, HEIGHT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pvp_button.collidepoint(event.pos):
                    game_mode = "PVP"
                    difficulty_level = 1
                    grid_size = get_grid_size(difficulty_level)
                    grid = create_grid(grid_size)
                elif pvai_button.collidepoint(event.pos):
                    game_mode = "PVA"
                    difficulty_level = None  # Reset difficulty level
    elif game_mode == "PVA" and grid is None:
        go_back_button, slider_rect, confirm_button = draw_difficulty_screen(screen, COLORS, FONT, WIDTH, HEIGHT, difficulty_level or 1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if go_back_button.collidepoint(event.pos):
                    game_mode = None
                elif slider_rect.collidepoint(event.pos):
                    difficulty_level = (event.pos[0] - (WIDTH // 2 - 150)) // 75 + 1
                    difficulty_level = max(1, min(difficulty_level, 5))
                    go_back_button, slider_rect, confirm_button = draw_difficulty_screen(screen, COLORS, FONT, WIDTH, HEIGHT, difficulty_level)
                elif confirm_button.collidepoint(event.pos):
                    if difficulty_level:
                        grid_size = get_grid_size(difficulty_level)
                        grid = create_grid(grid_size)
    else:
        screen.fill(COLORS['background'])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN and player_turn:
                x, y = pygame.mouse.get_pos()
                col = x // (WIDTH // grid_size)
                row = y // (HEIGHT // grid_size)
                
                if 0 <= row < grid_size and 0 <= col < grid_size:
                    if is_valid_selection(row, col):
                        selected_cells.append((row, col))
                        current_word += grid[row][col]['letter']
                        message = ""
                        
                        if check_word():
                            selected_cells = []
                            current_word = ""
                            player_turn = False
                    else:
                        message = "Invalid selection!"
                        
        if game_mode == "PVA" and not player_turn:
            ai_turn()
        
        draw_grid()
        go_back_button = draw_ui()
        pygame.display.flip()

pygame.quit()
sys.exit()