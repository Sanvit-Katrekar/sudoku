import solver
import random

def generate(boardLength=9,
             filled=40, #The numbers filled in the final unsolved puzzle
             toFill=15, #For generating solved puzzle
             logs=True, #For displaying logs to console
             ):
    solver.logs = logs

    toRemove = boardLength**2 - filled

    puzzle = [[0 for i in range(boardLength)]for j in range(boardLength)]

    empty = []


    for i in range(boardLength):

        for j in range(boardLength):

            if puzzle[i][j] == 0: empty.append((i, j))
            
    for i in range(toFill):

        while True:

            row, col = random.choice(empty)

            num = random.randint(1, 9)

            if solver.isValid(puzzle, num, (row, col)): break

        empty.remove((row, col))

        puzzle[row][col] = num

    solver.displayBoard(puzzle)
    
    if not solver.SolveBoard(puzzle):

        print('** Couldn\'t find solution! **')

        generate(boardLength=boardLength, filled=filled, toFill=toFill)

    solved = [list(row) for row in puzzle]

    filledSpots = []

    for i in range(boardLength):

        filledSpots.extend([(i, j) for j in range(boardLength)])

    for i in range(toRemove):
        row, col = random.choice(filledSpots)
        puzzle[row][col] = 0
        filledSpots.remove((row, col))
    
    return puzzle, solved

if __name__ == '__main__':
    x = generate()[0]
    solver.displayBoard(x)




