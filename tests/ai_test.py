from ai import isNotOnRow, isNotOnColumn, isNotOnSquare, isInBox, findBoxRow, findBoxColumn, findTwoOnBoxRow, findTwoOnBoxColumn, isNumInColumn, isNumInRow
from data import board


def test_isNotOnRow():
    assert isNotOnRow(board[0], 2) == False
    assert isNotOnRow(board[0], 9) == True
    assert isNotOnRow(board[0], 6) == True
    assert isNotOnRow(board[0], 1) == False


def test_isNotOnColumn():
    assert isNotOnColumn(0, 9) == False
    assert isNotOnColumn(0, 1) == True
    assert isNotOnColumn(0, 1) == True
    assert isNotOnColumn(0, 2) == False


def test_isNotOnSquare():
    assert isNotOnSquare(0, 0, 3) == False
    assert isNotOnSquare(5, 5, 1) == True
    assert isNotOnSquare(8, 8, 1) == True
    assert isNotOnSquare(8, 0, 2) == False


def test_findBoxRow():
    assert findBoxRow(3, 0, 0) == 0
    assert findBoxRow(2, 0, 1) == 2
    assert findBoxRow(6, 2, 0) == 1


def test_findBoxColumn():
    assert findBoxColumn(3, 0, 0) == 0
    assert findBoxColumn(2, 0, 1) == 2
    assert findBoxColumn(6, 2, 0) == 0


def test_findTwoOnBowRow():
    assert findTwoOnBoxRow(0) == [1, 3, 4]
    assert findTwoOnBoxRow(1) == [6, 9]
    assert findTwoOnBoxRow(2) == [5, 7, 9]


def test_findTwoOnBowColumn():
    assert findTwoOnBoxColumn(0) == [2, 6, 9]
    assert findTwoOnBoxColumn(1) == [1, 8]
    assert findTwoOnBoxColumn(2) == [4, 5, 6]


def testisNumInColumn():
    assert isNumInColumn(1, 0) == False
    assert isNumInColumn(2, 0) == True
    assert isNumInColumn(3, 0) == True
    assert isNumInColumn(4, 0) == False
    assert isNumInColumn(5, 0) == False
    assert isNumInColumn(6, 0) == True
    assert isNumInColumn(7, 0) == True
    assert isNumInColumn(8, 0) == True
    assert isNumInColumn(9, 0) == True


def testisNumInRow():
    assert isNumInRow(1, 0) == True
    assert isNumInRow(2, 0) == True
    assert isNumInRow(3, 0) == True
    assert isNumInRow(4, 0) == False
    assert isNumInRow(5, 0) == False
    assert isNumInRow(6, 0) == False
    assert isNumInRow(7, 0) == False
    assert isNumInRow(8, 0) == True
    assert isNumInRow(9, 0) == False
