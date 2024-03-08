from ai import *
from data import possibleChoices
def addNonZeroValuesToChoices(currentBoard):
    board = currentBoard
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                possibleChoices[i][j] = board[i][j]


# replace zeros with empty space
def replaceZeros(currentBoard):
    board = currentBoard
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                board[i][j] = " "


def fillChoices(x, y, currentBoard):
    board = currentBoard
    final = []
    for i in range(1, 10):
        if isNotOnRow(board[y], i):
            if isNotOnColumn(x, i, currentBoard):
                if isNotOnSquare(x, y, i, currentBoard):
                    final.append(i)
    return final



def fillChoicesTable(currentBoard):
    board = currentBoard
    for i in range(9):
        for j in range(9):
            if board[j][i] == " ":
                possibleChoices[j][i] = fillChoices(i, j, board)


def addCorrectValuesToBoard(currentBoard):
    board = currentBoard
    for i in range(9):
        for j in range(9):
            if board[i][j] == " ":
                if len(possibleChoices[i][j]) == 1:
                    board[i][j] = possibleChoices[i][j][0]


def requiredValue(xBox, yBox, currentBoard):
    board = currentBoard
    neededNumbers = []
    for i in range(1, 10):
        if not isInBox(i, xBox, yBox, currentBoard):
           neededNumbers.append(i)

    for num in neededNumbers:
        count = 0
        correctSpot = []
        for x in range(3):
            for y in range(3):
                if board[(yBox*3) + x][(xBox*3)+y] == ' ':
                    if not isNumInColumn(num, (xBox*3) + y, currentBoard):
                        if not isNumInRow(num, (yBox*3) + x, currentBoard):
                            count += 1
                            correctSpot = [x, y]

        if count == 1:
            board[(yBox*3) + correctSpot[0]][(xBox*3) + correctSpot[1]] = num


def notDone(currentBoard):
    board = currentBoard
    for i in range(9):
        for j in range(9):
            if board[i][j] == " ":
                return True
    return False