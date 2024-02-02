from ai import *
def addValues():
    for i in range(9):
        for j in range(9):
            if layers[i][j] != 0:
                possibleChoices[i][j] = layers[i][j]


# replace zeros with empty space
def replaceZeros():
    for i in range(9):
        for j in range(9):
            if layers[i][j] == 0:
                layers[i][j] = " "




def fillChoices(x, y):
    final = []
    for i in range(1, 10):
        if isNotOnRow(layers[y], i):
            if isNotOnColumn(x, i):
                if isNotonSquare(x, y, i):
                    final.append(i)
    return final



def fillChoicesTable():
    for i in range(9):
        for j in range(9):
            if layers[j][i] == " ":
                possibleChoices[j][i] = fillChoices(i, j)


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