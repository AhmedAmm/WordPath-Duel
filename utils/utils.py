def check_word(grid, selected_cells, current_word, overall_score, valid_words_found, WORD_LIST):
    word = current_word.upper()
    
    if word in WORD_LIST and word not in valid_words_found:
        score = sum(grid[r][c]['score'] for r, c in selected_cells)
        overall_score += score
        valid_words_found.add(word)
        message = f"Found {word}! +{score} points"
        return True, overall_score, valid_words_found, message
    return False, overall_score, valid_words_found, ""

def is_valid_selection(selected_cells, new_row, new_col):
    if not selected_cells:
        return new_row == 0 and new_col == 0  #(0,0)
    
    last_row, last_col = selected_cells[-1]
    return abs(new_row - last_row) + abs(new_col - last_col) == 1
