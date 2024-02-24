from ai import *
from logic import *

addValues()
replaceZeros()
print(makeMsg())
count = 0


while notDone():
    for i in range(3):
        rowTrick(i)
    for i in range(3):
        columnTrick(i)
    fillChoicesTable()
    makePerm()
    count += 1
    if count > 100:
        print("Took too long")
        break


print(makeMsg())
print(count)


# Notes
# Each square has a list of possible number choices.
# It goes through each square and checks how many choices each square has.
# Any square that only has one possible choice is updated to that choice
# The program then dumbs the old possible choices list and makes a new one.
# Later versions of the program could be more smart about updating the lists rather than making new ones
# The program will continue the process of hunting single choice squares until all squares have final numbers.
