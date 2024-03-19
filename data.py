board = [
    [1, 3, 0, 5, 0, 0, 0, 7, 0],
    [0, 0, 0, 0, 3, 0, 0, 0, 2],
    [7, 6, 0, 9, 0, 0, 5, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 0, 3],
    [9, 0, 0, 0, 0, 3, 0, 8, 0],
    [0, 0, 0, 0, 9, 1, 0, 0, 4],
    [8, 7, 0, 6, 0, 0, 3, 0, 5],
    [0, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 0, 9, 1, 5, 0, 0, 0, 6]
]

# this is just to make adding a new board easier. Just cp the array and copy it over the board and add values manually

sudoku_array = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

possibleChoices = [
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []]
]


def makeMsg():
    msg = "---------------------------------------\n"
    msg += "| " + str(board[0][0]) + " | " + str(board[0][1]) + " | " + str(board[0][2]) + " || " + str(
        board[0][3]) + " | " + str(board[0][4]) + " | " + str(board[0][5]) + " || " + str(
        board[0][6]) + " | " + str(board[0][7]) + " | " + str(board[0][8]) + " |\n"
    msg += "| " + str(board[1][0]) + " | " + str(board[1][1]) + " | " + str(board[1][2]) + " || " + str(
        board[1][3]) + " | " + str(board[1][4]) + " | " + str(board[1][5]) + " || " + str(
        board[1][6]) + " | " + str(board[1][7]) + " | " + str(board[1][8]) + " |\n"
    msg += "| " + str(board[2][0]) + " | " + str(board[2][1]) + " | " + str(board[2][2]) + " || " + str(
        board[2][3]) + " | " + str(board[2][4]) + " | " + str(board[2][5]) + " || " + str(
        board[2][6]) + " | " + str(board[2][7]) + " | " + str(board[2][8]) + " |\n"
    msg += "---------------------------------------\n"
    msg += "| " + str(board[3][0]) + " | " + str(board[3][1]) + " | " + str(board[3][2]) + " || " + str(
        board[3][3]) + " | " + str(board[3][4]) + " | " + str(board[3][5]) + " || " + str(
        board[3][6]) + " | " + str(board[3][7]) + " | " + str(board[3][8]) + " |\n"
    msg += "| " + str(board[4][0]) + " | " + str(board[4][1]) + " | " + str(board[4][2]) + " || " + str(
        board[4][3]) + " | " + str(board[4][4]) + " | " + str(board[4][5]) + " || " + str(
        board[4][6]) + " | " + str(board[4][7]) + " | " + str(board[4][8]) + " |\n"
    msg += "| " + str(board[5][0]) + " | " + str(board[5][1]) + " | " + str(board[5][2]) + " || " + str(
        board[5][3]) + " | " + str(board[5][4]) + " | " + str(board[5][5]) + " || " + str(
        board[5][6]) + " | " + str(board[5][7]) + " | " + str(board[5][8]) + " |\n"
    msg += "---------------------------------------\n"
    msg += "| " + str(board[6][0]) + " | " + str(board[6][1]) + " | " + str(board[6][2]) + " || " + str(
        board[6][3]) + " | " + str(board[6][4]) + " | " + str(board[6][5]) + " || " + str(
        board[6][6]) + " | " + str(board[6][7]) + " | " + str(board[6][8]) + " |\n"
    msg += "| " + str(board[7][0]) + " | " + str(board[7][1]) + " | " + str(board[7][2]) + " || " + str(
        board[7][3]) + " | " + str(board[7][4]) + " | " + str(board[7][5]) + " || " + str(
        board[7][6]) + " | " + str(board[7][7]) + " | " + str(board[7][8]) + " |\n"
    msg += "| " + str(board[8][0]) + " | " + str(board[8][1]) + " | " + str(board[8][2]) + " || " + str(
        board[8][3]) + " | " + str(board[8][4]) + " | " + str(board[8][5]) + " || " + str(
        board[8][6]) + " | " + str(board[8][7]) + " | " + str(board[8][8]) + " |\n"
    msg += "---------------------------------------\n"
    return msg