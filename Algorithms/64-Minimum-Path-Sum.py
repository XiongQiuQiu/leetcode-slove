'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r, c = len(grid), len(grid[0])
        dp = [i for i in grid[0]]
        for i in range(1,c):
            dp[i] = dp[i-1]+grid[0][i]
        for row in range(1,r):
            dp[0] = dp[0] + grid[row][0]
            for col in range(1, c):
                dp[col] = min(dp[col], dp[col - 1]) + grid[row][col]
        return dp[-1]
