board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 4, 0, 7, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def print_board(bo):
    for row in range(len(bo)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - -")

        for col in range(len(bo[0])):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")
            if col == 8:
                print(bo[row][col])
            else:
                print(str(bo[row][col]) + " ", end="")


def find_empty(bo):
    for row in range(len(bo)):
        for col in range(len(bo[0])):
            if bo[row][col] == 0:
                return row, col
