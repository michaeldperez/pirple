BOARD = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '], # row 1
    [' ', ' ', ' ', ' ', ' ', ' ', ' '], # row 2
    [' ', ' ', ' ', ' ', ' ', ' ', ' '], # row 3
    [' ', ' ', ' ', ' ', ' ', ' ', ' '], # row 4
    [' ', ' ', ' ', ' ', ' ', ' ', ' '], # row 5
    [' ', ' ', ' ', ' ', ' ', ' ', ' '], # row 6
    [' ', ' ', ' ', ' ', ' ', ' ', ' ']  # row 7
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
        column_selected.append(icon)
        return True
    else:
        return False

def draw_board(board):
  for row in range(6):
    for column in range(7):
      if column < 6:
        if column == 0:
          print('|{} |'.format(board[row][column]), end='')
        else:
          print(' {} |'.format(board[row][column]), end='')
      else:
        print(' {} |'.format(board[row][column]), end='\n')
