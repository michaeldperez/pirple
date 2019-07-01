from termcolor import colored

BOARD = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '], # row 1
    [' ', ' ', ' ', ' ', ' ', ' ', ' '], # row 2
    [' ', ' ', ' ', ' ', ' ', ' ', ' '], # row 3
    [' ', ' ', ' ', ' ', ' ', ' ', ' '], # row 4
    [' ', ' ', ' ', ' ', ' ', ' ', ' '], # row 5
    [' ', ' ', ' ', ' ', ' ', ' ', ' '], # row 6
]

CURRENT_PLAYER = 1

def toggle_player(current_player):
    return (1, 2)[current_player == 1]

def player_icon(current_player):
    icon = ('O', 'X')[current_player == 1]
    color = ('blue', 'red')[icon == 'X']
    return colored(icon, color)

def lenth_of_column(board, column):
    count = 0
    for row in board:
        if row[column] != ' ':
            count += 1
    return count

def able_to_move(board, column):
    return lenth_of_column(board, column) < 6

def place_token(board, column, icon):
    for row in board[::-1]:
        if row[column] == ' ':
            row[column] = icon
            break

def move(board, column, icon):
    column_selected = column - 1
    if able_to_move(board, column_selected):
        place_token(board, column_selected, icon)
        return True
    else:
        return False

def get_move(current_player):
    return int(input('Player {} please select a column: '.format(current_player)))

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

def check_column(board, column, icon):
    count = 0
    for row in range(6):
        if board[row][column] == icon:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    return False

def check_row(board, row, icon):
    count = 0
    for column in range(7):
        if board[row][column] == icon:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    return False

def check_all(board, icon, position_function):
    bounds = (7, 6)[position_function == check_row]
    return True in [position_function(board, position, icon) for position in range(bounds)]

def check_in_bounds(row, column):
    return row >= 0 and row < 6 and column >= 0 and column < 7

def check_diags(board, icon):
    for row in range(6):
        for column in range(7):
            count = 1
            for i in range(1,3):
                if check_in_bounds(row - i, column - 1):
                    if board[row - i][column - i] == icon:
                        count += 1
                        if count == 4:
                            return True
                if check_in_bounds(row + i, column + i):
                    if board[row + i][column + i] == icon:
                        count += 1
                        if count == 4:
                            return True
            count = 1
            for i in range(1, 3):
                if check_in_bounds(row - i, column + i):
                    if board[row - i][column + i] == icon:
                        count += 1
                        if count == 4:
                            return True
                if check_in_bounds(row + i, column - i):
                    if board[row + i][column - i] == icon:
                        count += 1
                        if count == 4:
                            return True
    return False

def check_win(board, icon, *position_functions):
    win = check_diags(BOARD, icon)
    if not win:
        for position_function in position_functions:
            if check_all(BOARD, icon, position_function):
                win = True
                break
    return win
    
def play(board, current_player):
    win = False
    while not win:
        draw_board(board)
        icon = player_icon(current_player)
        potential_move = get_move(current_player)
        valid_move = move(board, potential_move, icon)
        if valid_move:
            win = check_win(board, icon, check_row, check_column)
        else:
            print("That move is invalid, please try again.")
            continue
        if not win:
            current_player = toggle_player(current_player)
    draw_board(board)
    print('Player {} wins!'.format(current_player))

if __name__ == '__main__':
    play(BOARD, CURRENT_PLAYER)
