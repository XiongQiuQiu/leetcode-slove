def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    dp = [[1 if j == 0 else 0 for i in range(len(s) + 1)] for j in range(len(t) + 1)]
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if s[j - 1] == t[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]
    return dp[-1][-1]
s = "rabbbit"
t = "rabbit"
numDistinct(s,t)