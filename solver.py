##board = [
##    [5, 0, 0, 0, 4, 7, 2, 1, 0],
##    [0, 0, 0, 6, 1, 0, 4, 3, 0],
##    [3, 1, 4, 0, 5, 0, 0, 0, 0],
##    [0, 5, 0, 0, 0, 0, 0, 0, 3],
##    [9, 0, 8, 0, 6, 5, 1, 4, 0],
##    [0, 7, 0, 1, 0, 0, 0, 0, 0],
##    [0, 0, 0, 0, 3, 1, 9, 0, 8],
##    [1, 2, 3, 0, 0, 0, 5, 0, 0],
##    [0, 0, 9, 0, 7, 2, 3, 6, 0]
##    ]

board = [
    [0, 0, 8, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 4, 0, 0, 0, 0, 3],
    [4, 3, 0, 0, 0, 0, 0, 5, 0],
    [0, 2, 0, 0, 9, 6, 1, 7, 0],
    [3, 0, 0, 0, 0, 2, 0, 0, 0],
    [8, 0, 0, 0, 7, 0, 0, 0, 4],
    [0, 0, 1, 7, 0, 0, 0, 0, 0],
    [0, 0, 5, 0, 0, 0, 6, 0, 0],
    [0, 8, 0, 0, 6, 4, 2, 1, 0]
    ]


def displayBoard(Board, n=''):
    if not logs:
        return
    
    for i in range(len(Board)):

        print()

        if i != 0 and  i % 3 == 0: print(' - ' * len(Board))

        for j in range(len(Board)):

            if j != 0 and j % 3 == 0: print(' | ' , end = ' ')

            print(Board[i][j], end = ' ')

            

    print('\n\n\n_____________________________________   %s' % n, end = '\n')

def findEmpty(Board):

    for i in range(len(Board)):

        for j in range(len(Board[i])):

            if Board[i][j] == 0: return (i, j)

    return False


def isValid(Board, val, pos):

    blockLength = int(len(Board)**0.5)

    y, x = [i//3 for i in pos]

    block = [Board[y*blockLength + i][x*blockLength: x*blockLength + blockLength] for i in range(blockLength)]

    column = [row[pos[1]] for row in Board]

    if any([
            val in Board[pos[0]],#Checking if the number already exists in the row
            val in column,#Checking if the number already exists in the column
            any([val in i for i in block]) #Checking if the number already exists in the block
        ]): 

        return False
            
    return True


step = 0

def SolveBoard(Board):

    global step

    step += 1

    found = findEmpty(Board)

    if not found:

        displayBoard(Board, 'Solved!')

        return True

    row, col = found

    for i in range(1, len(Board) + 1):

        if isValid(Board, val = i, pos = (row, col)):

            Board[row][col] = i

            if SolveBoard(Board):

                return True

            Board[row][col] = 0

    return False

if __name__ == '__main__':
    logs = True
    if not SolveBoard(board):
        print('Couldn\'t find solution!\nSolution does not exist')


    



