def playing_board(rows, columns):
    row_range = rows + rows - 1
    col_range = 2 * columns
    for row in range(row_range):
        if row % 2 == 0:
            for column in range(1,col_range):
                if column % 2 == 1:
                    if column != (col_range - 1):
                        print(" ", end = "")
                    else:
                        print(" ")
                else:
                    print("|", end = "")
        else:
            print("-" * (col_range - 1))

playing_board(3,4)