import random
#
# layer1Input = input("What are the first 9 number on the top row, 1,2,3,4,5,0,0,8,9: ")
# layer1Striped = layer1Input.split(",")
# layer1 = [2]
# layer1 = list(map(int, layer1Striped))
#
# layer2Input = input("What are the first 9 number on the top row, 1,2,3,4,5,0,0,8,9: ")
# layer2Striped = layer2Input.split(",")
# layer2 = list(map(int, layer2Striped))
#
# layer3Input = input("What are the first 9 number on the top row, 1,2,3,4,5,0,0,8,9: ")
# layer3Striped = layer3Input.split(",")
# layer3 = list(map(int, layer3Striped))
#
# layer4Input = input("What are the first 9 number on the top row, 1,2,3,4,5,0,0,8,9: ")
# layer4Striped = layer4Input.split(",")
# layer4 = list(map(int, layer4Striped))
#
# layer5Input = input("What are the first 9 number on the top row, 1,2,3,4,5,0,0,8,9: ")
# layer5Striped = layer5Input.split(",")
# layer5 = list(map(int, layer5Striped))
#
# layer6Input = input("What are the first 9 number on the top row, 1,2,3,4,5,0,0,8,9: ")
# layer6Striped = layer1Input.split(",")
# layer6 = list(map(int, layer6Striped))
#
# layer7Input = input("What are the first 9 number on the top row, 1,2,3,4,5,0,0,8,9: ")
# layer7Striped = layer7Input.split(",")
# layer7 = list(map(int, layer7Striped))
#
# layer8Input = input("What are the first 9 number on the top row, 1,2,3,4,5,0,0,8,9: ")
# layer8Striped = layer8Input.split(",")
# layer8 = list(map(int, layer8Striped))
#
# layer9Input = input("What are the first 9 number on the top row, 1,2,3,4,5,0,0,8,9: ")
# layer9Striped = layer9Input.split(",")
# layer9 = list(map(int, layer9Striped))

# hard coded test values
layers = [
    [0, 0, 4, 7, 1, 0, 0, 0, 0],
    [0, 7, 2, 8, 0, 6, 5, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 7],
    [0, 1, 0, 6, 9, 0, 2, 0, 0],
    [3, 9, 0, 0, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 5],
    [0, 0, 1, 2, 3, 0, 8, 0, 4],
    [0, 0, 3, 5, 0, 4, 0, 0, 2],
    [2, 4, 0, 9, 0, 0, 0, 0, 0]
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
def addValues():
    for i in range(9):
        for j in range(9):
            if layers[i][j] != 0:
                possibleChoices[i][j] = layers[i][j]


addValues()


# replace zeros with empty space
def replaceZeros():
    for i in range(9):
        for j in range(9):
            if layers[i][j] == 0:
                layers[i][j] = " "


replaceZeros()

# print board
msg = "---------------------------------------\n"
msg += "| " + str(layers[0][0]) + " | " + str(layers[0][1]) + " | " + str(layers[0][2]) + " || " + str(layers[0][3]) + " | " + str(layers[0][4]) + " | " + str(layers[0][5]) + " || " + str(layers[0][6]) + " | " + str(layers[0][7]) + " | " + str(layers[0][8]) + " |\n"
msg += "| " + str(layers[1][0]) + " | " + str(layers[1][1]) + " | " + str(layers[1][2]) + " || " + str(layers[1][3]) + " | " + str(layers[1][4]) + " | " + str(layers[1][5]) + " || " + str(layers[1][6]) + " | " + str(layers[1][7]) + " | " + str(layers[1][8]) + " |\n"
msg += "| " + str(layers[2][0]) + " | " + str(layers[2][1]) + " | " + str(layers[2][2]) + " || " + str(layers[2][3]) + " | " + str(layers[2][4]) + " | " + str(layers[2][5]) + " || " + str(layers[2][6]) + " | " + str(layers[2][7]) + " | " + str(layers[2][8]) + " |\n"
msg += "---------------------------------------\n"
msg += "| " + str(layers[3][0]) + " | " + str(layers[3][1]) + " | " + str(layers[3][2]) + " || " + str(layers[3][3]) + " | " + str(layers[3][4]) + " | " + str(layers[3][5]) + " || " + str(layers[3][6]) + " | " + str(layers[3][7]) + " | " + str(layers[3][8]) + " |\n"
msg += "| " + str(layers[4][0]) + " | " + str(layers[4][1]) + " | " + str(layers[4][2]) + " || " + str(layers[4][3]) + " | " + str(layers[4][4]) + " | " + str(layers[4][5]) + " || " + str(layers[4][6]) + " | " + str(layers[4][7]) + " | " + str(layers[4][8]) + " |\n"
msg += "| " + str(layers[5][0]) + " | " + str(layers[5][1]) + " | " + str(layers[5][2]) + " || " + str(layers[5][3]) + " | " + str(layers[5][4]) + " | " + str(layers[5][5]) + " || " + str(layers[5][6]) + " | " + str(layers[5][7]) + " | " + str(layers[5][8]) + " |\n"
msg += "---------------------------------------\n"
msg += "| " + str(layers[6][0]) + " | " + str(layers[6][1]) + " | " + str(layers[6][2]) + " || " + str(layers[6][3]) + " | " + str(layers[6][4]) + " | " + str(layers[6][5]) + " || " + str(layers[6][6]) + " | " + str(layers[6][7]) + " | " + str(layers[6][8]) + " |\n"
msg += "| " + str(layers[7][0]) + " | " + str(layers[7][1]) + " | " + str(layers[7][2]) + " || " + str(layers[7][3]) + " | " + str(layers[7][4]) + " | " + str(layers[7][5]) + " || " + str(layers[7][6]) + " | " + str(layers[7][7]) + " | " + str(layers[7][8]) + " |\n"
msg += "| " + str(layers[8][0]) + " | " + str(layers[8][1]) + " | " + str(layers[8][2]) + " || " + str(layers[8][3]) + " | " + str(layers[8][4]) + " | " + str(layers[8][5]) + " || " + str(layers[8][6]) + " | " + str(layers[8][7]) + " | " + str(layers[8][8]) + " |\n"
msg += "---------------------------------------\n"
print(msg)


def isNotOnRow(row, num):
    for i in row:
        if num == i:
            return False
    return True





def isNotOnColumn(column, num):
    for i in range(9):
        if num == layers[i][column]:
            return False
    return True



def isNotonSquare(x, y, num):
    if 0 <= x < 3:
        x = 0
    elif 3 <= x < 6:
        x = 3
    else:
        x = 6
    if 0 <= y < 3:
        y = 0
    elif 3 <= y < 6:
        y = 3
    else:
        y = 6
    for i in range(3):
        for j in range(3):
            if num == layers[i+y][j+x]:
                return False
    return True


def fillChoices(x, y):
    final = []
    for i in range(1, 10):
        if isNotOnRow(layers[y], i):
            if isNotOnColumn(x, i):
                if isNotonSquare(x, y, i):
                    final.append(i)
    return final



def fillChoicesTable():
    # possibleChoices = [
    #     [[], [], [], [], [], [], [], [], []],
    #     [[], [], [], [], [], [], [], [], []],
    #     [[], [], [], [], [], [], [], [], []],
    #     [[], [], [], [], [], [], [], [], []],
    #     [[], [], [], [], [], [], [], [], []],
    #     [[], [], [], [], [], [], [], [], []],
    #     [[], [], [], [], [], [], [], [], []],
    #     [[], [], [], [], [], [], [], [], []],
    #     [[], [], [], [], [], [], [], [], []]
    # ]
    # addValues()
    for i in range(9):
        for j in range(9):
            if layers[j][i] == " ":
                possibleChoices[j][i] = fillChoices(i, j)


fillChoicesTable()


def makePerm():
    for i in range(9):
        for j in range(9):
            if layers[i][j] == " ":
                if len(possibleChoices[i][j]) == 1:
                    layers[i][j] = possibleChoices[i][j][0]




def printThings():
    for i in range(9):
        for j in range(9):
            print(possibleChoices[i][j], end=" ")
        print()

def notDone():
    for i in range(9):
        for j in range(9):
            if layers[i][j] == " ":
                return True
    return False

count = 0
while notDone():
    fillChoicesTable()
    makePerm()
    count+=1
    if count > 100:
        print("Took too long")
        break







msg = "---------------------------------------\n"
msg += "| " + str(layers[0][0]) + " | " + str(layers[0][1]) + " | " + str(layers[0][2]) + " || " + str(layers[0][3]) + " | " + str(layers[0][4]) + " | " + str(layers[0][5]) + " || " + str(layers[0][6]) + " | " + str(layers[0][7]) + " | " + str(layers[0][8]) + " |\n"
msg += "| " + str(layers[1][0]) + " | " + str(layers[1][1]) + " | " + str(layers[1][2]) + " || " + str(layers[1][3]) + " | " + str(layers[1][4]) + " | " + str(layers[1][5]) + " || " + str(layers[1][6]) + " | " + str(layers[1][7]) + " | " + str(layers[1][8]) + " |\n"
msg += "| " + str(layers[2][0]) + " | " + str(layers[2][1]) + " | " + str(layers[2][2]) + " || " + str(layers[2][3]) + " | " + str(layers[2][4]) + " | " + str(layers[2][5]) + " || " + str(layers[2][6]) + " | " + str(layers[2][7]) + " | " + str(layers[2][8]) + " |\n"
msg += "---------------------------------------\n"
msg += "| " + str(layers[3][0]) + " | " + str(layers[3][1]) + " | " + str(layers[3][2]) + " || " + str(layers[3][3]) + " | " + str(layers[3][4]) + " | " + str(layers[3][5]) + " || " + str(layers[3][6]) + " | " + str(layers[3][7]) + " | " + str(layers[3][8]) + " |\n"
msg += "| " + str(layers[4][0]) + " | " + str(layers[4][1]) + " | " + str(layers[4][2]) + " || " + str(layers[4][3]) + " | " + str(layers[4][4]) + " | " + str(layers[4][5]) + " || " + str(layers[4][6]) + " | " + str(layers[4][7]) + " | " + str(layers[4][8]) + " |\n"
msg += "| " + str(layers[5][0]) + " | " + str(layers[5][1]) + " | " + str(layers[5][2]) + " || " + str(layers[5][3]) + " | " + str(layers[5][4]) + " | " + str(layers[5][5]) + " || " + str(layers[5][6]) + " | " + str(layers[5][7]) + " | " + str(layers[5][8]) + " |\n"
msg += "---------------------------------------\n"
msg += "| " + str(layers[6][0]) + " | " + str(layers[6][1]) + " | " + str(layers[6][2]) + " || " + str(layers[6][3]) + " | " + str(layers[6][4]) + " | " + str(layers[6][5]) + " || " + str(layers[6][6]) + " | " + str(layers[6][7]) + " | " + str(layers[6][8]) + " |\n"
msg += "| " + str(layers[7][0]) + " | " + str(layers[7][1]) + " | " + str(layers[7][2]) + " || " + str(layers[7][3]) + " | " + str(layers[7][4]) + " | " + str(layers[7][5]) + " || " + str(layers[7][6]) + " | " + str(layers[7][7]) + " | " + str(layers[7][8]) + " |\n"
msg += "| " + str(layers[8][0]) + " | " + str(layers[8][1]) + " | " + str(layers[8][2]) + " || " + str(layers[8][3]) + " | " + str(layers[8][4]) + " | " + str(layers[8][5]) + " || " + str(layers[8][6]) + " | " + str(layers[8][7]) + " | " + str(layers[8][8]) + " |\n"
msg += "---------------------------------------\n"
print(msg)


# Notes
# Each square has a list of possible number choices.
# It goes through each square and checks how many choices each square has.
# Any square that only has one possible choice is updated to that choice
# The program then dumbs the old possible choices list and makes a new one.
# Later versions of the program could be more smart about updating the lists rather than making new ones
# The program will continue the process of hunting single choice squares until all squares have final numbers.
