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


def makeMsg(currentBoard):
    msg = "---------------------------------------\n"
    msg += "| " + str(currentBoard[0][0]) + " | " + str(currentBoard[0][1]) + " | " + str(currentBoard[0][2]) + " || " + str(
        currentBoard[0][3]) + " | " + str(currentBoard[0][4]) + " | " + str(currentBoard[0][5]) + " || " + str(
        currentBoard[0][6]) + " | " + str(currentBoard[0][7]) + " | " + str(currentBoard[0][8]) + " |\n"
    msg += "| " + str(currentBoard[1][0]) + " | " + str(currentBoard[1][1]) + " | " + str(currentBoard[1][2]) + " || " + str(
        currentBoard[1][3]) + " | " + str(currentBoard[1][4]) + " | " + str(currentBoard[1][5]) + " || " + str(
        currentBoard[1][6]) + " | " + str(currentBoard[1][7]) + " | " + str(currentBoard[1][8]) + " |\n"
    msg += "| " + str(currentBoard[2][0]) + " | " + str(currentBoard[2][1]) + " | " + str(currentBoard[2][2]) + " || " + str(
        currentBoard[2][3]) + " | " + str(currentBoard[2][4]) + " | " + str(currentBoard[2][5]) + " || " + str(
        currentBoard[2][6]) + " | " + str(currentBoard[2][7]) + " | " + str(currentBoard[2][8]) + " |\n"
    msg += "---------------------------------------\n"
    msg += "| " + str(currentBoard[3][0]) + " | " + str(currentBoard[3][1]) + " | " + str(currentBoard[3][2]) + " || " + str(
        currentBoard[3][3]) + " | " + str(currentBoard[3][4]) + " | " + str(currentBoard[3][5]) + " || " + str(
        currentBoard[3][6]) + " | " + str(currentBoard[3][7]) + " | " + str(currentBoard[3][8]) + " |\n"
    msg += "| " + str(currentBoard[4][0]) + " | " + str(currentBoard[4][1]) + " | " + str(currentBoard[4][2]) + " || " + str(
        currentBoard[4][3]) + " | " + str(currentBoard[4][4]) + " | " + str(currentBoard[4][5]) + " || " + str(
        currentBoard[4][6]) + " | " + str(currentBoard[4][7]) + " | " + str(currentBoard[4][8]) + " |\n"
    msg += "| " + str(currentBoard[5][0]) + " | " + str(currentBoard[5][1]) + " | " + str(currentBoard[5][2]) + " || " + str(
        currentBoard[5][3]) + " | " + str(currentBoard[5][4]) + " | " + str(currentBoard[5][5]) + " || " + str(
        currentBoard[5][6]) + " | " + str(currentBoard[5][7]) + " | " + str(currentBoard[5][8]) + " |\n"
    msg += "---------------------------------------\n"
    msg += "| " + str(currentBoard[6][0]) + " | " + str(currentBoard[6][1]) + " | " + str(currentBoard[6][2]) + " || " + str(
        currentBoard[6][3]) + " | " + str(currentBoard[6][4]) + " | " + str(currentBoard[6][5]) + " || " + str(
        currentBoard[6][6]) + " | " + str(currentBoard[6][7]) + " | " + str(currentBoard[6][8]) + " |\n"
    msg += "| " + str(currentBoard[7][0]) + " | " + str(currentBoard[7][1]) + " | " + str(currentBoard[7][2]) + " || " + str(
        currentBoard[7][3]) + " | " + str(currentBoard[7][4]) + " | " + str(currentBoard[7][5]) + " || " + str(
        currentBoard[7][6]) + " | " + str(currentBoard[7][7]) + " | " + str(currentBoard[7][8]) + " |\n"
    msg += "| " + str(currentBoard[8][0]) + " | " + str(currentBoard[8][1]) + " | " + str(currentBoard[8][2]) + " || " + str(
        currentBoard[8][3]) + " | " + str(currentBoard[8][4]) + " | " + str(currentBoard[8][5]) + " || " + str(
        currentBoard[8][6]) + " | " + str(currentBoard[8][7]) + " | " + str(currentBoard[8][8]) + " |\n"
    msg += "---------------------------------------\n"
    return msg