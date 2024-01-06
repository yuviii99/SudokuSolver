board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(bo):
    # A recursive approach involving backtracking
    # Base Case
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True

            bo[row][col] = 0
    return False


def valid(bo, number, position):
    # Check in the row
    for i in range(len(bo[0])):
        if bo[position[0]][i] == number and position[1] != i:
            return False

    # Check in the col
    for i in range(len(bo)):
        if bo[i][position[1]] == number and position[0] != i:
            return False

    # Check in the 3x3 box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == number and (i, j) != position:
                return False

    return True


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
    return None


print_board(board)
print("                       ")
solve(board)
print_board(board)
