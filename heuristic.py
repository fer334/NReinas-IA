import timeit
import numpy as np

previous_col = np.inf
debug = False
printHash = False


def generate_random_int(max, min):
    # return Math.floor(Math.random() * (max - min)) + min;
    return int(np.floor(np.random.rand() * (max - min) + min))

def print_board(board):
    N = len(board)
    for row in range(N):
        for col in range(N):
            if printHash:
                print("Q" if board[row][col]==-1 else "#", end=" ")
            else:
                print("Q" if board[row][col]==-1 else board[row][col], end=" ")

        print()

def locate_queens(board):
    N = len(board)
    for i in range(N):
        board[generate_random_int(0,N)][i] = -1

def calc_conflicts(board):
    N = len(board)
    # print('board', board)
    def fill_cols(row, col):
        # print()
        for i in range(N):
            # print(row, i ,board[row][i], end=" * ", sep=" ")
            if board[row][i] != -1:
                board[row][i] += 1
    def fill_rows(row, col):
        for i in range(N):
            if board[i][col] != -1:
                board[i][col] += 1
    def fill_diags(row, col):
        i = 1
        while not (row + i >= N or col + i >= N):
            if board[row + i][col + i] != -1:
                board[row + i][col + i] += 1
            i += 1
        i = 1
        while not (row - i < 0 or col - i < 0):
            if board[row - i][col - i] != -1:
                board[row - i][col - i] += 1
            i += 1
        i = 1
        while not (row + i >= N or col - i < 0):
            if board[row + i][col - i] != -1:
                board[row + i][col - i] += 1
            i += 1
        i = 1
        while not (row - i < 0 or col + i >= N):
            if board[row - i][col + i] != -1:
                board[row - i][col + i] += 1
            i += 1
    
    for row in range(N):
        for col in range(N):
            if board[row][col] != -1:
                board[row][col] = 0
    # print('aueao',board)
    for col in range(N):
        for row in range(N):
            if board[row][col] == -1:
                fill_cols(row, col)
                fill_rows(row, col)
                fill_diags(row, col)
    # print('hola',board)
    

def iterate(board):
    N = len(board)
    def min_conflict():
        global previous_col
        min = np.inf
        minPos = []

        for i in range(N):
            for j in range(N):
                if board[i][j] < min and board[i][j] != -1:
                    min = board[i][j]
                    minPos = [{ "i": i, "j": j }]
                elif board[i][j] == min:
                    minPos.append({ "i": i, "j": j })
                    
        res = minPos[generate_random_int(0, len(minPos))]
        if (previous_col == res["j"]):
            board[res["i"]][res["j"]] = 999999
            return min_conflict()
    
        previous_col = res["j"]
        # print('El min es: ', res)
        return res

    def queenPosFromCol(pos):
        row = pos["i"]
        col = pos["j"]
        for i in range(N):
            if board[i][col] == -1:
                return { "i": i, "j": col }

    def moveQueen(from_pos, to_pos):
        board[from_pos["i"]][from_pos["j"]] = 0
        board[to_pos["i"]][to_pos["j"]] = -1

    calc_conflicts(board)
    # print('chau',board)
    if debug:
        print("######Antes de mover")
        print_board(board)
    pos = min_conflict()
    queenPos = queenPosFromCol(pos)
    # print('queenPos', queenPos)
    moveQueen(queenPos, pos)
    if (debug):
        print("######Despues de mover")
        print_board(board)

def is_solved(board):
    N = len(board)

    def queensOnRow(row,col):
        queens=0
        for i in range(N):
            if board[row][i] == -1 and i != col:
                queens += 1
        return queens
            
    def queensOnColumn(row,col):
        queens = 0
        for i in range(N):
            if board[i][col] == -1 and i != row:
                queens += 1
        return queens
    def queensOnDiagonal(row,col):
        queens = 0
        i=1
        while (not (row + i >= N or col + i >= N)):
            if (board[row + i][col + i] == -1):
                queens+=1
            i+=1
        i = 1
        while (not(row - i < 0 or col - i < 0)):
            if (board[row - i][col - i] == -1):
                queens+=1
            i+=1
        
        i = 1
        while (not(row + i >= N or col - i < 0)):
            if (board[row + i][col - i] == -1):
                queens+=1
            i+=1

        i = 1
        while (not(row - i < 0 or col + i >= N)):
            if (board[row - i][col + i] == -1):
                queens+=1
            i+=1
        
        return queens
    for i in range(N):
        for j in range(N):
            if board[i][j] == -1:
                attackQueens = queensOnColumn(i, j) + queensOnRow(i, j) + queensOnDiagonal(i, j)
                if attackQueens != 0:
                    return False
    return True

def n_queens(N):
    board = np.zeros((N, N), dtype=int)
    locate_queens(board)
    nodes = 0
    start = timeit.default_timer()
    while(not is_solved(board)):
        iterate(board)
        nodes += 1
    stop = timeit.default_timer()
    print("Nodes: ", nodes)
    print("Time: ", stop - start)


n_queens(100)