from sudokuSolver.ai import isNotOnRow, isNotOnColumn, isNotOnSquare, isInBox, findBoxRow, findBoxColumn, findTwoOnBoxRow, findTwoOnBoxColumn, isNumInColumn, isNumInRow

board = [
    [3, 0, 0, 8, 0, 1, 0, 0, 2],
    [2, 0, 1, 0, 3, 0, 6, 0, 4],
    [0, 0, 0, 2, 0, 4, 0, 0, 0],
    [8, 0, 9, 0, 0, 0, 1, 0, 6],
    [0, 6, 0, 0, 0, 0, 0, 5, 0],
    [7, 0, 2, 0, 0, 0, 4, 0, 9],
    [0, 0, 0, 5, 0, 9, 0, 0, 0],
    [9, 0, 4, 0, 8, 0, 7, 0, 5],
    [6, 0, 0, 1, 0, 7, 0, 0, 3]
]

board2 = [
    [2, 0, 0, 3, 0, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 4, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 8, 0, 0, 1, 3, 6, 0],
    [1, 7, 0, 0, 0, 0, 0, 0, 0],
    [3, 6, 0, 8, 0, 0, 0, 0, 0],
    [0, 9, 0, 1, 4, 7, 0, 2, 0],
    [6, 3, 0, 0, 2, 0, 0, 4, 1],
    [0, 0, 0, 0, 0, 0, 9, 0, 0]
]

# expert board that cant be solved without guess func
board3 = [
    [0, 1, 3, 5, 9, 4, 8, 0, 0],
    [0, 5, 0, 8, 0, 3, 0, 4, 9],
    [9, 8, 4, 0, 2, 7, 0, 0, 0],
    [8, 3, 2, 0, 7, 5, 4, 9, 0],
    [0, 9, 0, 2, 4, 8, 0, 0, 0],
    [0, 4, 5, 3, 0, 9, 0, 0, 8],
    [4, 2, 9, 7, 3, 6, 1, 8, 5],
    [3, 7, 8, 4, 5, 1, 9, 0, 0],
    [5, 6, 1, 9, 8, 2, 3, 7, 4]
]
# expert board that cant be solved without guess func
board4 = [
    [0, 0, 0, 4, 0, 0, 0, 2, 5],
    [1, 4, 0, 2, 0, 7, 0, 0, 0],
    [2, 0, 8, 0, 0, 0, 1, 0, 4],
    [0, 0, 0, 0, 3, 9, 5, 0, 0],
    [9, 5, 3, 0, 0, 0, 4, 1, 7],
    [0, 0, 0, 0, 0, 0, 9, 0, 0],
    [8, 0, 0, 9, 0, 0, 0, 0, 0],
    [4, 0, 7, 0, 0, 5, 0, 0, 9],
    [0, 6, 9, 3, 0, 0, 2, 4, 0]
]

# expert board that cant be solved without guess func
board5 = [
    [5, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 5, 9],
    [4, 8, 2, 9, 7, 5, 0, 0, 0],
    [0, 0, 0, 0, 4, 8, 3, 2, 0],
    [8, 0, 4, 6, 0, 3, 0, 0, 0],
    [0, 3, 7, 0, 0, 0, 4, 0, 0],
    [0, 0, 0, 0, 0, 6, 5, 0, 0],
    [3, 4, 0, 5, 1, 0, 9, 0, 0],
    [0, 0, 5, 2, 0, 4, 0, 7, 0]
]


# expert board that cant be solved without guess func
board6 = [
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 5, 1, 0, 0, 0, 0],
    [7, 4, 8, 0, 0, 0, 1, 5, 3],
    [8, 0, 4, 0, 0, 0, 2, 6, 0],
    [0, 0, 0, 0, 7, 2, 4, 0, 8],
    [3, 2, 0, 0, 0, 8, 0, 0, 0],
    [0, 8, 2, 0, 0, 5, 0, 1, 9],
    [1, 0, 0, 0, 3, 0, 8, 7, 0],
    [0, 0, 0, 0, 0, 1, 6, 0, 0]
]

# this board required a shift in the guessing to solve
board7 = [
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

# hardest puzzle
board8 = [
    [0, 0, 0, 3, 0, 0, 0, 5, 0],
    [2, 0, 1, 4, 7, 5, 3, 9, 0],
    [0, 0, 0, 0, 0, 6, 0, 0, 4],
    [0, 0, 3, 8, 9, 0, 0, 0, 0],
    [6, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 6, 0, 0, 4, 9],
    [0, 5, 0, 0, 4, 0, 0, 6, 0],
    [0, 2, 0, 0, 0, 0, 0, 0, 5],
    [3, 0, 7, 0, 0, 0, 9, 0, 8]
]


def test_isNotOnRow():
    assert isNotOnRow(board[0], 1) == False
    assert isNotOnRow(board[0], 2) == False
    assert isNotOnRow(board[0], 3) == False
    assert isNotOnRow(board[0], 4) == True
    assert isNotOnRow(board[0], 5) == True
    assert isNotOnRow(board[0], 6) == True
    assert isNotOnRow(board[0], 7) == True
    assert isNotOnRow(board[0], 8) == False
    assert isNotOnRow(board[0], 9) == True


def test_isNotOnColumn():
    assert isNotOnColumn(0, 1, board) == True
    assert isNotOnColumn(0, 2, board) == False
    assert isNotOnColumn(0, 3, board) == False
    assert isNotOnColumn(0, 4, board) == True
    assert isNotOnColumn(0, 5, board) == True
    assert isNotOnColumn(0, 6, board) == False
    assert isNotOnColumn(0, 7, board) == False
    assert isNotOnColumn(0, 8, board) == False
    assert isNotOnColumn(0, 9, board) == False


def test_isNotOnSquare():
    assert isNotOnSquare(0, 0, 1, board) == False
    assert isNotOnSquare(0, 0, 2, board) == False
    assert isNotOnSquare(0, 0, 3, board) == False
    assert isNotOnSquare(0, 0, 4, board) == True
    assert isNotOnSquare(0, 0, 5, board) == True
    assert isNotOnSquare(0, 0, 6, board) == True
    assert isNotOnSquare(0, 0, 7, board) == True
    assert isNotOnSquare(0, 0, 8, board) == True
    assert isNotOnSquare(0, 0, 9, board) == True

def test_isInBox():
    assert isInBox(1, 0,0, board) == True
    assert isInBox(2, 0, 0, board) == True
    assert isInBox(3, 0, 0, board) == True
    assert isInBox(4, 0, 0, board) == False
    assert isInBox(5, 0, 0, board) == False
    assert isInBox(6, 0, 0, board) == False
    assert isInBox(7, 0, 0, board) == False
    assert isInBox(8, 0, 0, board) == False
    assert isInBox(9, 0, 0, board) == False



def test_findBoxRow():
    assert findBoxRow(3, 0, 0, board) == 0
    assert findBoxRow(2, 0, 1, board) == 2
    assert findBoxRow(6, 2, 0, board) == 1


def test_findBoxColumn():
    assert findBoxColumn(3, 0, 0, board) == 0
    assert findBoxColumn(2, 0, 1, board) == 2
    assert findBoxColumn(6, 2, 0, board) == 0


def test_findTwoOnBowRow():
    assert findTwoOnBoxRow(0, board) == [1, 3, 4]
    assert findTwoOnBoxRow(1, board) == [6, 9]
    assert findTwoOnBoxRow(2, board) == [5, 7, 9]


def test_findTwoOnBowColumn():
    assert findTwoOnBoxColumn(0, board) == [2, 6, 9]
    assert findTwoOnBoxColumn(1, board) == [1, 8]
    assert findTwoOnBoxColumn(2, board) == [4, 5, 6]


def testisNumInColumn():
    assert isNumInColumn(1, 0, board) == False
    assert isNumInColumn(2, 0, board) == True
    assert isNumInColumn(3, 0, board) == True
    assert isNumInColumn(4, 0, board) == False
    assert isNumInColumn(5, 0, board) == False
    assert isNumInColumn(6, 0, board) == True
    assert isNumInColumn(7, 0, board) == True
    assert isNumInColumn(8, 0, board) == True
    assert isNumInColumn(9, 0, board) == True


def testisNumInRow():
    assert isNumInRow(1, 0, board) == True
    assert isNumInRow(2, 0, board) == True
    assert isNumInRow(3, 0, board) == True
    assert isNumInRow(4, 0, board) == False
    assert isNumInRow(5, 0, board) == False
    assert isNumInRow(6, 0, board) == False
    assert isNumInRow(7, 0, board) == False
    assert isNumInRow(8, 0, board) == True
    assert isNumInRow(9, 0, board) == False
