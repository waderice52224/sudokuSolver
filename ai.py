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


def isInBox(num, xBox, yBox):
    xVal = 0
    yVal = 0
    if xBox == 1:
        xVal = 3
    elif xBox == 2:
        xVal = 6
    if yBox == 1:
        yVal = 3
    elif yBox == 2:
        yVal = 6
    for x in range(3):
        for y in range(3):
            if num == layers[y + yVal][x + xVal]:
                return True
    return False


def findBoxRow(num, xBox, yBox):
    xVal = 0
    yVal = 0
    if xBox == 1:
        xVal = 3
    elif xBox == 2:
        xVal = 6
    if yBox == 1:
        yVal = 3
    elif yBox == 2:
        yVal = 6
    for x in range(3):
        for y in range(3):
            if num == layers[y + yVal][x + xVal]:
                return y
    return -1


def findBoxColumn(num, xBox, yBox):
    xVal = 0
    yVal = 0
    if xBox == 1:
        xVal = 3
    elif xBox == 2:
        xVal = 6
    if yBox == 1:
        yVal = 3
    elif yBox == 2:
        yVal = 6
    for x in range(3):
        for y in range(3):
            if num == layers[y + yVal][x + xVal]:
                return x
    return -1

def findTwoOnBoxRow(boxRow):
    final = []
    for i in range(1, 10):
        count = 0
        for j in range(3):
            if isInBox(i, j, boxRow):
                count += 1
        if count == 2:
            final.append(i)
    return final


def findTwoOnBoxColumn(boxColumn):
    final = []
    for i in range(1, 10):
        count = 0
        for j in range(3):
            if isInBox(i, boxColumn, j):
                count += 1
        if count == 2:
            final.append(i)
    return final

# def rowHasOneSpot():
#


# These two functions seem to do what they were written to do, but it's unhelpful.
# def getAllPosibleRow(row):
#     final = []
#     for i in row:
#         if type(i) is not int:
#             for j in i:
#                 final.append(j)
#         else:
#             final.append(i)
#     return final
#
# def findSoloNums(nums):
#     print(nums)
#     final = []
#     for i in range(1, 10):
#         count = 0
#         for j in nums:
#             if i == j:
#                 count += 1
#         if count == 1:
#             final.append(i)
#     print(final)

