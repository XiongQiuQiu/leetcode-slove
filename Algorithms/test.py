s = "acdcb"
p = "a*c?b"


def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    length = len(p)
    dp = [True] + [False] * length
    for pattern in p:
        if pattern != '*':
            for n in reversed(range(length)):
                dp[n + 1] = dp[n] and (pattern == s[n] or pattern == '?')
        else:
            for n in range(1, length):
                dp[n] = dp[n - 1] or dp[n]
        dp[0] = dp[0] and pattern == '*'
    return dp[-1]
isMatch(s,p)