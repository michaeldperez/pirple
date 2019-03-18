BOARD = [
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

CURRENT_PLAYER = 1

def toggle_player(current_player):
    return (1, 2)[current_player == 1]

def player_icon(current_player):
    return ('O', 'X')[current_player == 1]

def able_to_move(column):
    return len(column) < 6

def move(board, column, icon):
    column_selected = board[column - 1]
    if able_to_move(column_selected):
        column_selected
    else:
        print('Invalid move. Please select again.')

