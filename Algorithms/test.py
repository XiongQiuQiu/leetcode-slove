def coinChange( coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    dp = [0] + [-1] * amount
    for i in range(1, amount + 1):
        if dp[i] <0:
            continue
        for coin in coins:
            if i + coin <= amount and (dp[i+coin]<0 or dp[i+coin] >dp[i]+1):
                dp[i+coin] = dp[i] +1
    return dp[-1]
coinChange([1,2,5],11)