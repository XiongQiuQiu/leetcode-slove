def maxProfit(prices, fee):
    """
    :type prices: List[int]
    :type fee: int
    :rtype: int
    """
    hold, sell = -float('inf'), 0
    for p in prices:
        hold = max(hold, sell - p - fee)
        sell = max(sell, hold + p)
    return sell

print(maxProfit([1, 3, 2, 8, 4, 9],2))

