from logic import *
from data import *
import copy
addNonZeroValuesToChoices(board)
replaceZeros(board)
print(makeMsg(board))



 # add a main fucntion that passes in the board for testing purposes.
def findNumbers(currentBoard):
    count = 0
    while notDone(currentBoard):
        for x in range(3):
            for y in range(3):
                requiredValue(y, x, currentBoard)
        fillChoicesTable(currentBoard)
        addCorrectValuesToBoard(currentBoard)
        count += 1
        if count >= 10:
            break


# def main(currentBoard):
#     findNumbers(currentBoard)
#     correctBoard = copy.deepcopy(currentBoard)
#     for i in range(1, 5):
#         for j in range(1, 5):
#             if i == 1:
#                 makePermGuessMaxHeads(currentBoard)
#             elif i == 2:
#                 makePermGuessMaxTails(currentBoard)
#             elif i == 3:
#                 makePermGuessMinHeads(currentBoard)
#             else:
#                 makePermGuessMinTails(currentBoard)
#             if j == 1:
#                 makePermGuessMaxHeads(currentBoard)
#             elif j == 2:
#                 makePermGuessMaxTails(currentBoard)
#             elif j == 3:
#                 makePermGuessMinHeads(currentBoard)
#             else:
#                 makePermGuessMinTails(currentBoard)
#             findNumbers(currentBoard)
#             if not notDone(currentBoard):
#                 print(makeMsg(currentBoard))
#             currentBoard = copy.deepcopy(correctBoard)


# main(board)

def mainRec(currentBoard, depth):
    findNumbers(currentBoard)
    correctBoard = copy.deepcopy(currentBoard)
    for i in range(2):
        for j in range(2):
            if i == 0:
                makePermGuessMaxHeads(currentBoard)
                if j == 0:
                    makePermGuessMinHeads(currentBoard)
                else:
                    makePermGuessMinTails(currentBoard)
            else:
                makePermGuessMaxTails(currentBoard)
                if j == 0:
                    makePermGuessMinHeads(currentBoard)
                else:
                    makePermGuessMinTails(currentBoard)
        findNumbers(currentBoard)
        if not notDone(currentBoard):
            print(depth)
            return currentBoard
        elif depth == 2:
            return None
        else:
            mainRec(currentBoard, depth + 1)
        currentBoard = copy.deepcopy(correctBoard)


print(makeMsg(mainRec(board, 0)))


# if board is finished
    # return the board and print the depth
# elif board is not finished but the depth is too big
    # return void
# else
    # call function with depth+1





# findNumbers(board)
# if not notDone(board):
#     print(makeMsg())
#     print(1)
# correctBoard = board
# if notDone(board):
#     makePermGuessMaxHeads(board)
#     findNumbers(board)
#     if not notDone(board):
#         print(makeMsg())
#         print(2)
# board = correctBoard
# if notDone(board):
#     makePermGuessMaxTails(board)
#     findNumbers(board)
#     if not notDone(board):
#         print(makeMsg())
#         print(3)
# board = correctBoard
# if notDone(board):
#     makePermGuessMinHeads(board)
#     findNumbers(board)
#     if not notDone(board):
#         print(makeMsg())
#         print(4)
# board = correctBoard
# if notDone(board):
#     makePermGuessMinTails(board)
#     findNumbers(board)
#     if not notDone(board):
#         print(makeMsg())
#         print(5)

# Notes
# Each square has a list of possible number choices.
# It goes through each square and checks how many choices each square has.
# Any square that only has one possible choice is updated to that choice
# The program then dumbs the old possible choices list and makes a new one.
# Later versions of the program could be more smart about updating the lists rather than making new ones
# The program will continue the process of hunting single choice squares until all squares have final numbers.
