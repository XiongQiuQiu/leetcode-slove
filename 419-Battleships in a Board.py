class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ans = 0
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == 'X':
                    if x > 0 and board[x - 1][y] == 'X':
                        continue
                    if y > 0 and board[x][y - 1] == 'X':
                        continue
                    ans += 1
        return ans
