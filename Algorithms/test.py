def change(amount, coins):
    """
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:
        for i in range(1, amount + 1):
            if i >= c:
                dp[i] += dp[i - c]
    return dp[-1]
change(5,[1, 2, 5])