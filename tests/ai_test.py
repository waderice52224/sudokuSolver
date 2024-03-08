from ai import isNotOnRow, isNotOnColumn, isNotOnSquare, isInBox, findBoxRow, findBoxColumn, findTwoOnBoxRow, findTwoOnBoxColumn, isNumInColumn, isNumInRow


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


def test_isNotOnRow():
    assert isNotOnRow(board[0], 2) == False
    assert isNotOnRow(board[0], 9) == True
    assert isNotOnRow(board[0], 6) == True
    assert isNotOnRow(board[0], 1) == False


def test_isNotOnColumn():
    assert isNotOnColumn(0, 9, board) == False
    assert isNotOnColumn(0, 1, board) == True
    assert isNotOnColumn(0, 1, board) == True
    assert isNotOnColumn(0, 2, board) == False


def test_isNotOnSquare():
    assert isNotOnSquare(0, 0, 3, board) == False
    assert isNotOnSquare(5, 5, 1, board) == True
    assert isNotOnSquare(8, 8, 1, board) == True
    assert isNotOnSquare(8, 0, 2, board) == False

def test_isInBox():
    assert isInBox(4, 0,0, board) == False
    assert isInBox(1, 0,0, board) == True
    assert isInBox(2, 0,0, board) == True
    assert isInBox(5, 0,0, board) == False



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
