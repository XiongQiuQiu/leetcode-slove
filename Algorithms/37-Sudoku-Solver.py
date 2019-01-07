'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
'''
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()

    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    return row, col
        return -1, -1

    def solve(self):
        row, col = self.findUnassigned()
        if row == -1 and col == -1:
            return True
        for num in map(str, range(1, 10)):
            if self.issafe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = '.'
        return False

    def issafe(self, row, col, ch):
        if self.checkcol(col, ch) and self.checkrow(row, ch) and self.checksquare(col, row, ch):
            return True
        return False

    def checkcol(self, col, ch):
        for row in range(9):
            if ch == self.board[row][col]:
                return False
        return True

    def checkrow(self, row, ch):
        if ch in self.board[row]:
            return False
        return True

    def checksquare(self, col, row, ch):
        square = [i for c1 in self.board[row / 3 * 3:(row / 3 + 1) * 3]
                  for i in c1[col / 3 * 3:(col / 3 + 1) * 3]]
        if ch in square:
            return False
        return True


class Solution(object):
    # def solveSudoku(self, board):
    # """
    # :type board: List[List[str]]
    # :rtype: void Do not return anything, modify board in-place instead.
    # """
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        ##
        row = []
        col = []
        diag = [[0] * 3 for _ in xrange(3)]
        for i in xrange(9):
            row.append(set(list(xrange(1, 10))))
            col.append(set(list(xrange(1, 10))))
            diag[i / 3][i % 3] = set(list(xrange(1, 10)))

        consider = set()
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == ".":
                    consider.add((i, j))
                else:
                    c = int(board[i][j])
                    if c in row[i]:
                        row[i].remove(c)
                    if c in col[j]:
                        col[j].remove(c)
                    if c in diag[i / 3][j / 3]:
                        diag[i / 3][j / 3].remove(c)

        self.dfs(row, col, diag, consider, board)

    def dfs(self, row, col, diag, consider, board):
        if len(consider) == 0:
            return True

        maxpossible = 9
        for (r, c) in consider:
            possible = row[r] & col[c] & diag[r / 3][c / 3]
            if len(possible) <= maxpossible:  # such that we could consider the minimum each time and detect 0 earlier
                maxpossible = len(possible)
                i, j = r, c

        if maxpossible == 0:
            return False

        consider.remove((i, j))
        possible = row[i] & col[j] & diag[i / 3][j / 3]
        for num in possible:
            board[i][j] = str(num)
            row[i].remove(num)
            col[j].remove(num)
            diag[i / 3][j / 3].remove(num)
            if self.dfs(row, col, diag, consider, board):
                return True
            board[i][j] = "."
            row[i].add(num)
            col[j].add(num)
            diag[i / 3][j / 3].add(num)
        consider.add((i, j))
        return False
