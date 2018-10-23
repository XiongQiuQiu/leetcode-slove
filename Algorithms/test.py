def uniquePathsWithObstacles1(obstacleGrid):
    if not obstacleGrid:
        return 
    r, c = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0 for _ in xrange(c)] for _ in xrange(r)]
    dp[0][0] = 1 - obstacleGrid[0][0]
    for i in xrange(1, r):
        dp[i][0] = dp[i-1][0] * (1 - obstacleGrid[i][0])
    print dp
    for i in xrange(1, c):
        dp[0][i] = dp[0][i-1] * (1 - obstacleGrid[0][i])
    print dp
    for i in xrange(1, r):
        for j in xrange(1, c):
            dp[i][j] = (dp[i][j-1] + dp[i-1][j]) * (1 - obstacleGrid[i][j])
    return dp[-1][-1]

uniquePathsWithObstacles1([[0,0,0],[0,1,0],[0,0,0]])