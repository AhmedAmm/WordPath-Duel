import pygame
from utils.utils import is_valid_selection, check_word

def handle_player_turn(event, grid, grid_size, selected_cells, current_word, player_turn, message, overall_score, valid_words_found, WORD_LIST):
    x, y = pygame.mouse.get_pos()
    col = x // (800 // grid_size)
    row = y // (600 // grid_size)
    
    if 0 <= row < grid_size and 0 <= col < grid_size:
        if is_valid_selection(selected_cells, row, col):
            selected_cells.append((row, col))
            current_word += grid[row][col]['letter']
            message = ""
            
            if check_word(grid, selected_cells, current_word, overall_score, valid_words_found, WORD_LIST)[0]:
                selected_cells = []
                current_word = ""
                player_turn = False
        else:
            message = "Invalid selection!"
    return player_turn, selected_cells, current_word, message


def ai_turn(grid, grid_size, selected_cells, current_word, player_turn, message, overall_score, valid_words_found, WORD_LIST):
    from algorithms.minimax import Minimax
    minimax = Minimax(grid_size, grid_size)
    minimax.grid = [[grid[i][j]['letter'] for j in range(grid_size)] for i in range(grid_size)]
    score, move = minimax.minimax(0, 0, "")
    if move == 'D':
        selected_cells.append((selected_cells[-1][0] + 1, selected_cells[-1][1]))
    elif move == 'R':
        selected_cells.append((selected_cells[-1][0], selected_cells[-1][1] + 1))
    current_word += grid[selected_cells[-1][0]][selected_cells[-1][1]]['letter']
    if check_word(grid, selected_cells, current_word, overall_score, valid_words_found, WORD_LIST)[0]:
        selected_cells = []
        current_word = ""
    player_turn = True
    return player_turn, selected_cells, current_word, message