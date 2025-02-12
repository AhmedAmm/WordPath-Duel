import pygame
from settings import *

import pygame
from settings import *

def wrap_text(text, font, max_width):
    """
    Breaks the text into multiple lines so that each line's width is less than max_width.
    This is a simple implementation that splits the text character-by-character.
    """
    lines = []
    current_line = ""
    for char in text:
        test_line = current_line + char
        if font.size(test_line)[0] > max_width:
            if current_line:
                lines.append(current_line)
            current_line = char
        else:
            current_line = test_line
    if current_line:
        lines.append(current_line)
    return lines

def wrap_word_list(words, font, max_width):
    """
    Takes a list of words (strings) and groups them into lines where the total width of each line
    does not exceed max_width. Returns a list of strings, where each string is a line of words.
    """
    lines = []
    current_line = []
    current_width = 0
    space_width = font.size(" ")[0]
    
    for word in words:
        word_width = font.size(word)[0]
        # If adding this word exceeds max_width, push current_line to lines and start a new line.
        if current_line and current_width + space_width + word_width > max_width:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_width = word_width
        else:
            if current_line:
                current_width += space_width + word_width
            else:
                current_width = word_width
            current_line.append(word)
    
    if current_line:
        lines.append(" ".join(current_line))
    return lines

def draw_ui(screen, overall_score, current_word, message, valid_words_found, words):
    # Determine the UI area (reserved on the right)
    ui_x = WINDOW_WIDTH - UI_WIDTH
    ui_rect = pygame.Rect(ui_x, 0, UI_WIDTH, WINDOW_HEIGHT)
    
    # Draw a background for the UI area
    pygame.draw.rect(screen, (50, 50, 50), ui_rect)
    pygame.draw.rect(screen, COLORS['text'], ui_rect, 2)
    
    # Draw Score at the top of the UI area.
    score_text = FONT.render(f"Score: {overall_score}", True, COLORS['player'])
    screen.blit(score_text, (ui_x + 10, 20))
    
    # Wrap and draw the current word.
    max_text_width = UI_WIDTH - 20  # leave a 10px margin on each side
    current_word_full = "Current: " + current_word
    wrapped_lines = wrap_text(current_word_full, FONT, max_text_width)
    y_offset = 60
    for line in wrapped_lines:
        current_line_text = FONT.render(line, True, COLORS['text'])
        screen.blit(current_line_text, (ui_x + 10, y_offset))
        y_offset += FONT.get_linesize()
    
    # Draw message
    wrapped_message_text_lines = wrap_text(message, FONT, max_text_width)
    for line in wrapped_message_text_lines:
        curr_msg = FONT.render(line, True, COLORS['text'])
        screen.blit(curr_msg, (ui_x + 10, y_offset))
        y_offset += FONT.get_linesize()
    
    # Create a list of word-score strings (e.g., "abc(3)") and apply word wrapping on them.
    word_list = [f"{w}({s})" for w, s in words]
    wrapped_word_lines = wrap_word_list(word_list, FONT, max_text_width)
    words_y_offset = y_offset + 10 + FONT.get_linesize()  # start after message text
    for line in wrapped_word_lines:
        line_text = FONT.render(line, True, COLORS['text'])
        screen.blit(line_text, (ui_x + 10, words_y_offset))
        words_y_offset += FONT.get_linesize()
    
    # ---- New Section: Display Current Winner ----
    if overall_score > 0:
        winner_str = "Current Winner: Player"
    elif overall_score < 0:
        winner_str = "Current Winner: AI"
    else:
        winner_str = "Current Winner: Draw"
    
    # Apply word wrap to the winner text
    winner_lines = wrap_text(winner_str, FONT, max_text_width)
    winner_y_offset = words_y_offset + 10  # add a little spacing after the words list
    for line in winner_lines:
        line_text = FONT.render(line, True, COLORS['text'])
        screen.blit(line_text, (ui_x + 10, winner_y_offset))
        winner_y_offset += FONT.get_linesize()
    # ------------------------------------------------
    
    # Draw found words
    found_text = SMALL_FONT.render("Found: " + ", ".join(valid_words_found), True, COLORS['text'])
    screen.blit(found_text, (ui_x + 10, WINDOW_HEIGHT - 120))
    
    # Draw the "Go Back" button near the bottom of the UI area.
    go_back_text = FONT.render("Go Back", True, COLORS['text'])
    go_back_button = pygame.Rect(ui_x + 10, WINDOW_HEIGHT - 60, 100, 40)
    pygame.draw.rect(screen, COLORS['player'], go_back_button)
    pygame.draw.rect(screen, COLORS['text'], go_back_button, 2)
    go_back_text_rect = go_back_text.get_rect(center=go_back_button.center)
    screen.blit(go_back_text, go_back_text_rect)
    
    return go_back_button
