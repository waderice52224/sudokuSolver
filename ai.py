from data import *

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
