
import numpy as np
import math

def simulatedAnnealing(board):
    #print("----------------------------------------")
    T = 0
    t = 1
    tiredBound = 100000

    print("*******initial board*******")

    print(board)
    while True:
        if (isSolution(board) == True or t > tiredBound):
            print(t)
            return board
        T = schedule(t)

        boardPrime = makeRandomMove(board.copy())

        deltaFit = fitness(boardPrime) - fitness(board)
        if (deltaFit >0):
            board = boardPrime
        else:
            r =np.random.rand()
            if r < math.e**(deltaFit/T):
                board = boardPrime
        t+=1



def makeRandomMove(board):
    tempBoard = board.copy()
    rowToChange = np.random.randint(8)
    for i in range(8):
        if tempBoard[rowToChange,i] == 1:
           tempBoard[rowToChange,i] = 0
           tempBoard[rowToChange, np.random.randint(8)] = 1
           return tempBoard


def schedule(t):
    return 10000/t

def isSolution(board):
    if fitness(board) <9:
        return True
    return False

def generateRandomBoard():
    board = np.zeros((8,8), dtype=int)
    population_1D_vector = np.zeros(shape=(8,8))  # Each solution is represented as a row in this array. If there are 5 rows, then there are 5 solutions.
    QueenIndicies = np.random.rand(8) * 8
    QueenIndicies = QueenIndicies.astype(np.uint8)
    for i in range(0,8):
        board[i,QueenIndicies[i]] = 1
    return board

def fitness(tempBoard):
    board = tempBoard.copy()
    rowsWithQueens = {}
    colsWithQueens = {}
    northEastDiagonalsWithQueens = {}
    southEastDiagonalsWithQueens = {}
    for row in range(8):
        for col in range(8):
            if board[row][col] == 1:
                rowsWithQueens[row] = 1
                colsWithQueens[col] = 1
                northEastDiagonalsWithQueens[row + col] = 1
                southEastDiagonalsWithQueens[8 - 1 - row + col] = 1
    return len(rowsWithQueens)+ len(colsWithQueens)+ len(northEastDiagonalsWithQueens) + len(southEastDiagonalsWithQueens)



finalBoard = simulatedAnnealing(generateRandomBoard())

print("*******Final board*******")
print(finalBoard)
