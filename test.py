import copy

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]



def mainRec(currentBoard, depth):
    currentBoard[2][2] = 5
    correctBoard = copy.deepcopy(currentBoard)
    for i in range(2):
        for j in range(2):
            if i == 0:
                currentBoard[0][0] = 1
                if j == 0:
                    currentBoard[0][1] = 1
                else:
                    currentBoard[0][1] = 2
            else:
                currentBoard[0][2] = 1
                if j == 0:
                    currentBoard[1][0] = 1
                else:
                    currentBoard[1][0] = 2
        if depth == 4:
            return None
        else:
            print(depth)
            print(currentBoard)
            mainRec(currentBoard, depth + 1)
        currentBoard = copy.deepcopy(correctBoard)

mainRec(board, 0)