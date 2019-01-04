def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    rl, cl = len(board[0]), len(board)
    def dfs(board,rl, cl):
        for c in range(cl):
            for r in range(rl):
                tmp = board
                boardT = [[cl[i] for cl in board] for i in range(len(board))]
                if tmp[c][r] == '.':
                    for i in range(1, 10):
                        if i in board[c]:
                            continue
                        if i in boardT[r]:
                            continue
                        square = [i for c in tmp[c / 3 * 3:(c / 3 + 1) * 3]
                                  for i in tmp[c][r / 3 * 3:(r / 3 + 1) * 3]
                                  ]
                        if i in square:
                            continue
                        tmp[c][r] = i
                        if c == cl - 1 and r == rl - 1:
                            board = tmp
                        dfs(tmp[:],rl, cl)
solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])