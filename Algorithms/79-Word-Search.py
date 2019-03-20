'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''


'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        cl = len(board)
        rl = len(board[0]) if cl else 0
        for c in range(cl):
            for r in range(rl):
                if board[c][r] == word[0]:
                    if len(word) == 1: return True
                    if self.helper(board,(c,r,1),{(c, r)}, word, cl, rl):
                        return True
        return False

    def helper(self, board, point, vset,word, cl, rl):
        dz = zip((0, 1, 0, -1), (-1, 0, 1, 0))
        x, y, i = point
        for dx, dy in dz:
            nx, ny = dx + x, dy + y
            if 0 <= nx < cl and 0 <= ny < rl and (nx,ny) not in vset:
                if board[nx][ny] == word[i]:
                    if i == len(word) - 1:
                        return True
                    if self.helper(board,(nx,ny,i+1),vset|{(nx,ny)},word,cl,rl):
                        return True
        return False

def exist(self, board, word):
    if not board:
        return False
    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            if self.dfs(board, i, j, word):
                return True
    return False

# check whether can find word, start at (i,j) position
def dfs(self, board, i, j, word):
    if len(word) == 0: # all the characters are checked
        return True
    if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
        return False
    tmp = board[i][j]  # first character is found, check the remaining part
    board[i][j] = "#"  # avoid visit agian
    # check whether can find "word" along one direction
    res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
    or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
    board[i][j] = tmp
    return res
