# sudokuSolver

## Why I wrote this program

My cousin expressed interest in learning to code and I offered to help him through the basics. He also explained his interest in writing this program. As soon as he explained the program I was excited. I have always found number puzzles fun, so I knew that I would have a good time with this project. After I got the program solving all hard puzzles and some expert puzzles I realized that the program could solve puzzles better than I can. At this point I realized that if I wanted to make the program smarter... I myself, would have to get smarter too. I started studying advanced Sudoku and realized that the sudoku rabbit hole is deeper than I thought and getting smarter was going to be more involved than I thought.

At this point I realized that continuing work on this project would require a shift to studying sudoku and stopping progress on the code its self. This idea made me a little sad. I was having so much fun working on it that I knew that I needed another way to work on the progression of the project while I am studying sudoku. So I brainstormed ways to pivot, it came down to: code refactoring and readability improvements, writing a front end/ switching to Javascript, and writing test coverage for current functions and future functions for the advanced Sudoku techniques I am currently learning. I talked to one of my professors about it and they were able to explain that I should focus on things that I want to do for work. Of the three options I think software testing I something that I would love to do for work while I am growing into a better developer.

Where the programs stands today is continuing work on growing test coverage. I plan on overdoing it on the testing and having multiple different kinds of tests. I also want to get more creative on the individual tests. I think this will be required if I want any of the tests to fail. The program as of today is not capable of placing a wrong number, (at least in my testing so far), so a function is only called if it will be able to function correctly. The only way the program can fail is if the Sudoku is too hard. I want to prove that is the case. 

This project is completely my own, it's not homework, it has no imported libraries (other than testing), and has no other contributors. Any similarities to other software or programs is exciting because I have done zero research, other than testing once again. I am trying to grow a lot in that department. It's not that I am not growing in the coding department, I have grown a lot in [problem-solving](#problem-solving).
## Thought Process

### Paradigms
I decided to write the program procedurally because as class system is not applicable due to the fact that the only stored info is 81 numbers that look visually like an array. Making a board object is kind a just a slap in the face of the beautiful data structure that is arrays. Writing it functionally felt a little overkill, and maybe a little too wizardly. I feel like the program is very simple and with some refactors I think the program will be very elegant. As far as Imperative and Declarative go, they confuse me, so they will be tackled on other projects. 

### Why python
I am Studying Computer Science at USU, the way the CS department here at USU has decided to teach programing is with Python as the high level language and Java as the lower level Langauge. We also have started HTML/CSS/Javascript. 

Of all these options HTML/CSS/Javascript is tempting and may be switched to later. Java is not tempting at all due to the reasons stated above in [Paradigms](#paradigms). In the end my [cousin](#why-i-wrote-this-program) was the first reason I wrote the program and if I am going to be teaching basic coding principles, I think Python is the best language. 

### Approach
I took a very simple approach. I thought about how I play Sudoku and broke it down to rules, and each step for those said rules.

## What I have learned so far

### Code Quality
I am kinda disappointed how messy the code I write is. The first version of the program was completely unreadable and inconsistent. Frankly after the only refactor I have done, it's still a disaster. I am learning a few things about how to write code a little better on the first try. I am also getting a lot of practice refactoring my code.

### Tests
This program grew legs and ran towards being my testing lesson. My plans for the program is to 

### Problem solving
I did not really learn anything more about python in this program. As far as growing my hard skills, It was mostly [code quality](#code-quality), and my problem-solving ability. As I wrote the program I would finish a rule and test how much smarter the program had gotten. A big moment is when I started testing the program against hard puzzles. At first the program was very incapable. This is what pushed me to write requiredValue:
```
def requiredValue(xBox, yBox):
    neededNumbers = []
    for i in range(1, 10):
        if not isInBox(i, xBox, yBox):
           neededNumbers.append(i)

    for num in neededNumbers:
        count = 0
        correctSpot = []
        for x in range(3):
            for y in range(3):
                if board[(yBox*3) + x][(xBox*3)+y] == ' ':
                    if not isNumInColumn(num, (xBox*3) + y):
                        if not isNumInRow(num, (yBox*3) + x):
                            count += 1
                            correctSpot = [x,y]

        if count == 1:
            board[(yBox*3) + correctSpot[0]][(xBox*3) + correctSpot[1]] = num
```
I am particularly proud of this code because it launched the program past hard puzzles and into expert puzzles. Within library of puzzles I use to test it cannot solve all expert puzzles but all hard puzzles and some expert. This was a huge jump in intelligence from just one rule. This rule also made columnTrick and rowTrick outdated. It is just a smarter and more useful rule, while also being less code. 

## How to run
Currently the program is not user friendly. 
You will just need to run it from the terminal.
```
python main.py
```
This will run the program with the default puzzle. If you would like to change the puzzle, go to sudokuSolver/data.py and change the board to your puzzle. 0's represent unknown numbers. 




