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


def rowTrick(boxRow):
    twos = findTwoOnBoxRow(boxRow)
    fillBox = 0
    numPos = []
    row = 0
    for i in twos:
        for j in range(3):
            if not isInBox(i, j, boxRow):
                box = j
            else:
                numPos.append(findBoxRow(i, j, boxRow))
        for k in range(3):
            if k not in numPos:
                row = k
        layersRowValue = [layers[(boxRow * 3) + row][box * 3], layers[(boxRow * 3) + row][(box * 3) + 1],
                          layers[(boxRow * 3) + row][(box * 3) + 2]]
        count = 0
        for p in layersRowValue:
            if p == ' ':
                count += 1
        if count == 1:
            makePermRowTrick(i, box, row, boxRow)
        numPos = []




def makePermRowTrick(num, box, row, boxRow):
    layersRowValue = [layers[(boxRow * 3) + row][box * 3], layers[(boxRow * 3) + row][(box * 3) + 1], layers[(boxRow * 3) + row][(box * 3) + 2]]
    for i in layersRowValue:
        if i == ' ':
            layers[(boxRow * 3) + row][(box * 3) + layersRowValue.index(' ')] = num




def columnTrick(boxColumn):
    twos = findTwoOnBoxColumn(boxColumn)
    fillBox = 0
    numPos = []
    row = 0
    box = 0
    for i in twos:
        for j in range(3):
            if not isInBox(i, boxColumn, j):
                box = j
            else:
                numPos.append(findBoxColumn(i, boxColumn, j))
        for k in range(3):
            if k not in numPos:
                row = k
        layersColumnValue = [layers[box * 3][(boxColumn * 3) + row], layers[(box * 3) + 1][(boxColumn * 3) + row], layers[(box * 3) + 2][(boxColumn * 3) + row]]
        count = 0
        for p in layersColumnValue:
            if p == ' ':
                count += 1
        if count == 1:
            makePermColumnTrick(i, box, row, boxColumn)
        numPos = []


def makePermColumnTrick(num, box, row, boxColumn):
    layersColumnValue = [layers[box * 3][(boxColumn * 3) + row], layers[(box * 3) + 1][(boxColumn * 3) + row],layers[(box * 3) + 2][(boxColumn * 3) + row]]
    for i in layersColumnValue:
        if i == ' ':
            layers[(box * 3) + layersColumnValue.index(' ')][(boxColumn * 3) + row] = num

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