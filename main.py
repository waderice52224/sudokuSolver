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



# this code needs refactored. Its dirty and it is not solving all the puzzles it should. From here on out this funcion will be devolopled with TDD. I am sick of manually testing puzzles.
def mainRec(currentBoard, depth):
    findNumbers(currentBoard)
    for i in range(2):
        if i == 0:
            localPossibleChoices = fillChoicesTable(currentBoard)
            makePermGuessMaxHeads(currentBoard, localPossibleChoices)
        else:
            localPossibleChoices = fillChoicesTable(currentBoard)
            makePermGuessMaxTails(currentBoard, localPossibleChoices)
        findNumbers(currentBoard)
        if not notDone(currentBoard):
            print(depth)
            print(makeMsg(currentBoard))
            return currentBoard
        # elif boardMostlyFull(currentBoard):
        #     print("Duplicate")
        #     return None
        elif depth == 10:
            return None
        else:
            print(depth)
            print(makeMsg(currentBoard))
            mainRec(copy.deepcopy(currentBoard), depth + 1)



mainRec(board, 0)










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
