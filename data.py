layers = [
    [0, 0, 0, 1, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 0, 3, 0, 0],
    [4, 0, 0, 6, 2, 5, 1, 7, 0],
    [0, 0, 0, 8, 7, 0, 0, 0, 0],
    [5, 0, 9, 0, 0, 0, 0, 4, 0],
    [0, 0, 7, 0, 0, 3, 0, 0, 9],
    [0, 7, 0, 0, 0, 6, 0, 0, 3],
    [0, 5, 0, 0, 4, 0, 6, 0, 0],
    [0, 0, 4, 5, 0, 0, 7, 0, 0]
]

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
    msg += "| " + str(layers[0][0]) + " | " + str(layers[0][1]) + " | " + str(layers[0][2]) + " || " + str(
        layers[0][3]) + " | " + str(layers[0][4]) + " | " + str(layers[0][5]) + " || " + str(
        layers[0][6]) + " | " + str(layers[0][7]) + " | " + str(layers[0][8]) + " |\n"
    msg += "| " + str(layers[1][0]) + " | " + str(layers[1][1]) + " | " + str(layers[1][2]) + " || " + str(
        layers[1][3]) + " | " + str(layers[1][4]) + " | " + str(layers[1][5]) + " || " + str(
        layers[1][6]) + " | " + str(layers[1][7]) + " | " + str(layers[1][8]) + " |\n"
    msg += "| " + str(layers[2][0]) + " | " + str(layers[2][1]) + " | " + str(layers[2][2]) + " || " + str(
        layers[2][3]) + " | " + str(layers[2][4]) + " | " + str(layers[2][5]) + " || " + str(
        layers[2][6]) + " | " + str(layers[2][7]) + " | " + str(layers[2][8]) + " |\n"
    msg += "---------------------------------------\n"
    msg += "| " + str(layers[3][0]) + " | " + str(layers[3][1]) + " | " + str(layers[3][2]) + " || " + str(
        layers[3][3]) + " | " + str(layers[3][4]) + " | " + str(layers[3][5]) + " || " + str(
        layers[3][6]) + " | " + str(layers[3][7]) + " | " + str(layers[3][8]) + " |\n"
    msg += "| " + str(layers[4][0]) + " | " + str(layers[4][1]) + " | " + str(layers[4][2]) + " || " + str(
        layers[4][3]) + " | " + str(layers[4][4]) + " | " + str(layers[4][5]) + " || " + str(
        layers[4][6]) + " | " + str(layers[4][7]) + " | " + str(layers[4][8]) + " |\n"
    msg += "| " + str(layers[5][0]) + " | " + str(layers[5][1]) + " | " + str(layers[5][2]) + " || " + str(
        layers[5][3]) + " | " + str(layers[5][4]) + " | " + str(layers[5][5]) + " || " + str(
        layers[5][6]) + " | " + str(layers[5][7]) + " | " + str(layers[5][8]) + " |\n"
    msg += "---------------------------------------\n"
    msg += "| " + str(layers[6][0]) + " | " + str(layers[6][1]) + " | " + str(layers[6][2]) + " || " + str(
        layers[6][3]) + " | " + str(layers[6][4]) + " | " + str(layers[6][5]) + " || " + str(
        layers[6][6]) + " | " + str(layers[6][7]) + " | " + str(layers[6][8]) + " |\n"
    msg += "| " + str(layers[7][0]) + " | " + str(layers[7][1]) + " | " + str(layers[7][2]) + " || " + str(
        layers[7][3]) + " | " + str(layers[7][4]) + " | " + str(layers[7][5]) + " || " + str(
        layers[7][6]) + " | " + str(layers[7][7]) + " | " + str(layers[7][8]) + " |\n"
    msg += "| " + str(layers[8][0]) + " | " + str(layers[8][1]) + " | " + str(layers[8][2]) + " || " + str(
        layers[8][3]) + " | " + str(layers[8][4]) + " | " + str(layers[8][5]) + " || " + str(
        layers[8][6]) + " | " + str(layers[8][7]) + " | " + str(layers[8][8]) + " |\n"
    msg += "---------------------------------------\n"
    return msg