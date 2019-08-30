import sys


# function to print the board on to the console
def printFileBoard(board):
    print("*********************")
    for x in range(0, 9):
        if x == 3 or x == 6:
            print("*********************")
        for y in range(0, 9):
            if y == 3 or y == 6:
                print("*", end=" ")
            print(board[x][y], end=" ")
        print()
    print("*********************")

#Checks to see if the board still has empty spaces
def isFull(board):

    for x in range (0, 9):
        for y in range (0, 9):
            if board[x][y] == 0:
                return False
    return True

def possibleEnteries(board, i, j):

    # loads Dict with numbers form 1 to 9
    possibilityDict = {}
    for x in range(1,10):
        possibilityDict[x] = 0

    #For Horizontial enteries
    for y in range(0, 9):
        if not board[i][y] == 0:
            possibilityDict[board[i][j]] = 1

    #For vertical enteries
    for x in range(0, 9):
        if not board[x][j] == 0:
            possibilityDict[board[i][j]] = 1

    #For squares of 3x3
    #we declare k and l to make sure that we have the location of the top right on any square
    k=0
    l=0
    if i>=0 and i<=2:
        k=0
    elif i>=3 and i<=5:
        k=3
    else:
        k=6

    if j>=0 and j<=2:
        l=0
    elif j>=3 and j<=5:
        l=3
    else:
        l=6
    for x in range(k, k+3):
        for y in range(l, l+3):
            if not board[x][y] == 0:
                possibilityDict[board[i][j]] = 1

    for x in range (1,10):
        if possibilityDict[x] == 0:
            possibilityDict[x] = x
        else:
            possibilityDict[x] = 0
    return possibilityDict

def sudokuSolver(board):
    i=0
    j=0
    possibilities = {}

    #if board isnt full there is no need to continue
    if isFull(board):
        print("Solved!")
        printFileBoard(board)
        return
    else:
        # find the first vacant spot
        for x in range(0,9):
            for y in range (0,9):
                if board[x][y] == 0:
                    i=x
                    j=y
                    break
                else:
                    continue
                break

            # get all the possibilities for i,j
            possibilities = possibleEnteries(board, i , j)

            # go through all the possibilities adn call the function again and again
            for x in range(1, 10):
                if not possibilities[x] == 0:
                    board[i][j] = possibilities[x]
                    #The new board is called ie. recursive funciton
                    sudokuSolver(board)
            #backtrack
            board[i][j] = 0

def main():
    sudokuBoard = [ [6, 7, 8, 1, 4, 2, 9, 5, 3],
                    [9, 4, 1, 3, 7, 5, 2, 6, 8],
                    [2, 3, 5, 9, 8, 6, 4, 7, 1],
                    [8, 9, 6, 5, 3, 1, 7, 4, 2],
                    [7, 2, 3, 4, 9, 8, 6, 1, 5],
                    [1, 5, 4, 2, 6, 7, 3, 8, 9],
                    [3, 8, 9, 6, 5, 4, 1, 2, 7],
                    [4, 1, 7, 8, 2, 3, 5, 0, 6],
                    [5, 6, 2, 7, 1, 9, 0, 3, 4]]

    printFileBoard(sudokuBoard)
    sudokuSolver(sudokuBoard)

if __name__ == "__main__":

    main()
















