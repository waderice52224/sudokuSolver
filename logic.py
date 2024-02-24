from ai import *
def addNonZeroValuesToChoices():
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                possibleChoices[i][j] = board[i][j]


# replace zeros with empty space
def replaceZeros():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                board[i][j] = " "




def fillChoices(x, y):
    final = []
    for i in range(1, 10):
        if isNotOnRow(board[y], i):
            if isNotOnColumn(x, i):
                if isNotOnSquare(x, y, i):
                    final.append(i)
    return final



def fillChoicesTable():
    for i in range(9):
        for j in range(9):
            if board[j][i] == " ":
                possibleChoices[j][i] = fillChoices(i, j)


def addCorrectValuesToBoard():
    for i in range(9):
        for j in range(9):
            if board[i][j] == " ":
                if len(possibleChoices[i][j]) == 1:
                    board[i][j] = possibleChoices[i][j][0]


def rowTrick(boxRow):
    canidateNums = findTwoOnBoxRow(boxRow)
    numPos = []
    rowWithinTargetBox = 0
    for i in canidateNums:
        for j in range(3):
            if not isInBox(i, j, boxRow):
                targetBox = j
            else:
                numPos.append(findBoxRow(i, j, boxRow))
        for k in range(3):
            if k not in numPos:
                rowWithinTargetBox = k
        layersRowValue = [board[(boxRow * 3) + rowWithinTargetBox][targetBox * 3], board[(boxRow * 3) + rowWithinTargetBox][(targetBox * 3) + 1],
                          board[(boxRow * 3) + rowWithinTargetBox][(targetBox * 3) + 2]]
        count = 0
        for p in layersRowValue:
            if p == ' ':
                count += 1
        if count == 1:
            makePermRowTrick(i, targetBox, rowWithinTargetBox, boxRow)
        numPos = []



# both make perms can be imporoved if they accept rows and columns that have two empty spots and check next to the tartget cell to see if the num is on that row or column
def makePermRowTrick(num, targetBox, rowWithinTargetBox, boxRow):
    layersRowValue = [board[(boxRow * 3) + rowWithinTargetBox][targetBox * 3], board[(boxRow * 3) + rowWithinTargetBox][(targetBox * 3) + 1], board[(boxRow * 3) + rowWithinTargetBox][(targetBox * 3) + 2]]
    for i in layersRowValue:
        if i == ' ':
            board[(boxRow * 3) + rowWithinTargetBox][(targetBox * 3) + layersRowValue.index(' ')] = num




def columnTrick(boxColumn):
    canidateNums = findTwoOnBoxColumn(boxColumn)
    numPos = []
    rowWithinTargetBox = 0
    targetBox = 0
    for i in canidateNums:
        for j in range(3):
            if not isInBox(i, boxColumn, j):
                targetBox = j
            else:
                numPos.append(findBoxColumn(i, boxColumn, j))
        for k in range(3):
            if k not in numPos:
                rowWithinTargetBox = k
        layersColumnValue = [board[targetBox * 3][(boxColumn * 3) + rowWithinTargetBox], board[(targetBox * 3) + 1][(boxColumn * 3) + rowWithinTargetBox], board[(targetBox * 3) + 2][(boxColumn * 3) + rowWithinTargetBox]]
        count = 0
        for p in layersColumnValue:
            if p == ' ':
                count += 1
        if count == 1:
            makePermColumnTrick(i, targetBox, rowWithinTargetBox, boxColumn)
        numPos = []


def makePermColumnTrick(num, targetBox, rowWithinTargetBox, boxColumn):
    layersColumnValue = [board[targetBox * 3][(boxColumn * 3) + rowWithinTargetBox], board[(targetBox * 3) + 1][(boxColumn * 3) + rowWithinTargetBox], board[(targetBox * 3) + 2][(boxColumn * 3) + rowWithinTargetBox]]
    for i in layersColumnValue:
        if i == ' ':
            board[(targetBox * 3) + layersColumnValue.index(' ')][(boxColumn * 3) + rowWithinTargetBox] = num

# Test Function
# def printThings():
#     for i in range(9):
#         for j in range(9):
#             print(possibleChoices[i][j], end=" ")
#         print()


def notDone():
    for i in range(9):
        for j in range(9):
            if board[i][j] == " ":
                return True
    return False