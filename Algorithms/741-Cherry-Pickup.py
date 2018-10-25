'''

In a N x N grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.
Your task is to collect maximum number of cherries possible by following the rules below:

Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.
Example 1:
Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
Output: 5
Explanation:
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
Note:

grid is an N by N 2D array, with 1 <= N <= 50.
Each grid[i][j] is an integer in the set {-1, 0, 1}.
It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.
'''
class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        L = len(grid)
        dp = [[0 for _ in range(L)] for _ in range(L)]
        dp[0][0] = grid[0][0]
        for t in range(1,2*L-1):
            for i in range(L)[::-1]:
                for p in range(L)[::-1]:
                    j = t-i
                    q = t -p
                    if (j<0 or q <0 or j >= L or q >= L or grid[i][j] <0 or grid[p][q] < 0):
                        dp[i][p] = -1
                        continue
                    if i > 0:dp[i][p] = max(dp[i][p],dp[i-1][p])
                    if p > 0:dp[i][p] = max(dp[i][p],dp[i][p-1])
                    if i>0 and p>0:
                        dp[i][p] = max(dp[i][p],dp[i-1][p-1])
                    if dp[i][p] >= 0:
                        second = grid[p][q] if i != p else 0
                        dp[i][p] += grid[i][j] + second
        return max(dp[-1][-1],0)


class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = {}
        res = self.findMaxCherries(0, 0, 0, 0, dp, grid)
        return 0 if res == float('-inf') else res

    def findMaxCherries(self, i1, j1, i2, j2, dp, grid):
        if (i1, j1, i2, j2) in dp:
            return dp[(i1, j1, i2, j2)]
        n = len(grid)
        if i1 == n - 1 and j1 == n - 1 and i2 == n - 1 and j2 == n - 1:
            return grid[-1][-1]
        if i1 >= n or i2 >= n or j1 >= n or j2 >= n:
            return float('-inf')
        if grid[i1][j1] == -1 or grid[i2][j2] == -1:
            return float('-inf')
        best = max(
            self.findMaxCherries(i1 + 1, j1, i2 + 1, j2, dp, grid),
            self.findMaxCherries(i1 + 1, j1, i2, j2 + 1, dp, grid),
            self.findMaxCherries(i1, j1 + 1, i2 + 1, j2, dp, grid),
            self.findMaxCherries(i1, j1 + 1, i2, j2 + 1, dp, grid)
        )
        best += grid[i1][j1] if (i1, j1) == (i2, j2) else grid[i1][j1] + grid[i2][j2]
        dp[((i1, j1, i2, j2))] = best
        return best