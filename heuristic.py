import timeit
import numpy as np

def main(N, printMat=True, printHash=True):
    def generate_random_int(max, min):
        # return Math.floor(Math.random() * (max - min)) + min;
        return int(np.floor(np.random.rand() * (max - min) + min))
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
    def print_board(board):
        for row in range(N):
            for col in range(N):
                if printHash:
                    print("Q" if board[row][col]==-1 else "#", end=" ")
                else:
                    print("Q" if board[row][col]==-1 else board[row][col], end=" ")

            print()

    def generate_board():
        board = np.zeros((N, N), dtype=int)
        for i in range(N):
            board[generate_random_int(0,N)][i] = -1
        return board

    def calc_conflicts():
      

        for col in range(N):
            for row in range(N):
                if board[row][col] != -1:
                    board[row][col] = 0
                    board[row][col] += queensOnRow(row, col)
                    board[row][col] += queensOnColumn(row, col)
                    board[row][col] += queensOnDiagonal(row, col)

    def iterate():
        def min_conflict():
            min = np.inf
            minPos = []
            for i in range(N):
                for j in range(N):
                    if board[i][j] < min and board[i][j] != -1:
                        min = board[i][j]
                        minPos = [{ "i": i, "j": j }]
                    elif board[i][j] == min:
                        minPos.append({ "i": i, "j": j })
            # print(minPos)
            # print('ue','\n',board)
            return minPos[ generate_random_int(0,len(minPos)) ]
        def queenPosFromCol(pos):
            row = pos["i"]
            col = pos["j"]
            for i in range(N):
                if board[i][col] == -1:
                    return { "i": i, "j": col }
        def moveQueen(from_pos, to_pos):
            board[from_pos["i"]][from_pos["j"]] = 0
            board[to_pos["i"]][to_pos["j"]] = -1

        calc_conflicts()
        pos = min_conflict()
        queenPos = queenPosFromCol(pos)
        moveQueen(queenPos, pos)
        # if (printMat) console.log("######Despues de mover");
        if (printMat):
            print("######Despues de mover")
            print_board(board)

    def is_solved():
        for i in range(N):
            for j in range(N):
                if board[i][j] == -1:
                    attackQueens = queensOnColumn(i, j) + queensOnRow(i, j) + queensOnDiagonal(i, j)
                    if attackQueens != 0:
                       return False
        return True
    board = generate_board()
    # calc_conflicts()
    # print_board(board)
    # iterate()
    # iterate()
    nodes = 0
    start = timeit.default_timer()
    while(not is_solved()):
        iterate()
        nodes += 1
    stop = timeit.default_timer()
    print("Nodes: ", nodes)
    print("Time: ", stop - start)


main(80, printMat=False, printHash=False)