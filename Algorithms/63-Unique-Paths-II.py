'''A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid: return 0
        r,c= len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in obstacleGrid[0]] for _ in obstacleGrid]
        dp[0][0] =1- obstacleGrid[0][0]
        for row in range(1,r):
            dp[row][0] = dp[row-1][0]*(1-obstacleGrid[row][0])
        for col in range(1,c):
            dp[0][col] = dp[0][col-1] * (1-obstacleGrid[0][col])
        for row in range(1,r):
            for col in range(1,c):
                dp[row][col] = (dp[row-1][col]+dp[row][col-1]) * (1 - obstacleGrid[row][col])
        return dp[-1][-1]

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid: return 0
        r,c= len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * c
        dp[0] = 1- obstacleGrid[0][0]
        for col in range(1,c):
            dp[col] = dp[col-1] * (1-obstacleGrid[0][col])
        for row in range(1,r):
            dp[0] *= (1-obstacleGrid[row][0])
            for col in range(1,c):
                dp[col] = (dp[col-1]+dp[col]) * (1-obstacleGrid[row][col])
        return dp[-1]

# in place
def uniquePathsWithObstacles(self, obstacleGrid):
    if not obstacleGrid:
        return
    r, c = len(obstacleGrid), len(obstacleGrid[0])
    obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
    for i in xrange(1, r):
        obstacleGrid[i][0] = obstacleGrid[i-1][0] * (1 - obstacleGrid[i][0])
    for i in xrange(1, c):
        obstacleGrid[0][i] = obstacleGrid[0][i-1] * (1 - obstacleGrid[0][i])
    for i in xrange(1, r):
        for j in xrange(1, c):
            obstacleGrid[i][j] = (obstacleGrid[i-1][j] + obstacleGrid[i][j-1]) * (1 - obstacleGrid[i][j])
    return obstacleGrid[-1][-1]