from logic import *
from data import *

addNonZeroValuesToChoices(board)
replaceZeros(board)
print(makeMsg())



 # add a main fucntion that passes in the board for testing purposes.
def main(currentBoard):
    count = 0
    while notDone(currentBoard):
        for x in range(3):
            for y in range(3):
                requiredValue(y, x, currentBoard)
        fillChoicesTable(currentBoard)
        addCorrectValuesToBoard(currentBoard)
        count += 1
        if count >= 100:
            print("Took too long")
            break
    print(makeMsg())
    print(count)


makePermGuessMax(board)
main(board)
print("Board after Guess max")
print(makeMsg())


makePermGuessMin(board)
main(board)
print("Board after Guess min")
print(makeMsg())



# Notes
# Each square has a list of possible number choices.
# It goes through each square and checks how many choices each square has.
# Any square that only has one possible choice is updated to that choice
# The program then dumbs the old possible choices list and makes a new one.
# Later versions of the program could be more smart about updating the lists rather than making new ones
# The program will continue the process of hunting single choice squares until all squares have final numbers.
