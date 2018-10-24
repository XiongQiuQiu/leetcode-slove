def calculateMinimumH(dungeon):
    """
    :type dungeon: List[List[int]]
    :rtype: int
    """
    c = len(dungeon[0])
    dp = [float('inf')] * (c-1) + [1]
    for row in dungeon[::-1]:
        for col in range(c)[::-1]:
            dp[col] = max(min(dp[col:col+2])-row[col],1)
    return dp[0]

def calculateMinimumHP(dungeon):
    n = len(dungeon[0])
    need = [2**31] * (n-1) + [1]
    for row in dungeon[::-1]:
        for j in range(n)[::-1]:
            # print need[j]
            # print need[j+1]
            need[j] = max(min(need[j:j+2]) - row[j], 1)
    return need[0]
print calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]])