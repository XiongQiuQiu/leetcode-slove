'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
'''


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        vset = set()
        for r in range(1, len(board) - 1):
            for c in range(1, len(board[0]) - 1):
                if board[r][c] == 'O' and (r, c) not in vset:
                    self.dfs(vset, board, (r, c))

    def dfs(self, vset, board, point):
        dxs = [0, 1, 0, -1]
        dys = [1, 0, -1, 0]
        x, y = point[0], point[1]
        queue = [(x, y)]
        tmpset = {(x, y)}
        xl = len(board)
        yl = len(board[0])
        while queue:
            x, y = queue.pop()
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if 0 <= nx < xl and 0 <= ny < yl:
                    if board[nx][ny] == 'O' and (nx, ny) not in tmpset:
                        if nx in (0, xl - 1) or ny in (0, yl - 1):
                            vset.union(tmpset)
                            return
                        queue.append((nx, ny))
                        tmpset.add((nx, ny))
        for x, y in tmpset:
            board[x][y] = 'X'
        vset.union(tmpset)