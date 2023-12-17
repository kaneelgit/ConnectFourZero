import numpy as np

def board_state_int(board, current_player):

    board_state = np.zeros([5, 6, 3])

    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if col == 'X':
                board_state[r, c, 0] = 1
            if col == 'O':
                board_state[r, c, 1] = 2
            if col == ' ':
                board_state[r, c, 2] = current_player

    return board_state
