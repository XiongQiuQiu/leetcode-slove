def maxProfit4(self, k, prices):
    n = len(prices)
    if n < 2:
        return 0
    # k is big enougth to cover all ramps.
    if k >= n / 2:
        return sum(i - j
                   for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
    globalMax = [[0] * n for _ in xrange(k + 1)]
    for i in xrange(1, k + 1):
        # The max profit with i transations and selling stock on day j.
        localMax = [0] * n
        for j in xrange(1, n):
            profit = prices[j] - prices[j - 1]
            localMax[j] = max(
                # We have made max profit with (i - 1) transations in
                # (j - 1) days.
                # For the last transation, we buy stock on day (j - 1)
                # and sell it on day j.
                globalMax[i - 1][j - 1] + profit,
                # We have made max profit with (i - 1) transations in
                # (j - 1) days.
                # For the last transation, we buy stock on day j and
                # sell it on the same day, so we have 0 profit, apparently
                # we do not have to add it.
                globalMax[i - 1][j - 1],  # + 0,
                # We have made profit in (j - 1) days.
                # We want to cancel the day (j - 1) sale and sell it on
                # day j.
                localMax[j - 1] + profit)
            globalMax[i][j] = max(globalMax[i][j - 1], localMax[j])
    return globalMax[k][-1]




def maxProfit(self, k, prices):
    """
    :type k: int
    :type prices: List[int]
    :rtype: int
    """
    # The problem is hard
    # Time complexity, O(nk)
    # Space complexity, O(nk)
    length = len(prices)
    if length < 2:
        return 0
    max_profit = 0
    # if k>= n/2, then it can't complete k transactions. The problem becomes buy-and-sell problem 2
    if k >= length / 2:
        for i in xrange(1, length):
            max_profit += max(prices[i] - prices[i - 1], 0)
        return max_profit

    # max_global[i][j] is to store the maximum profit, at day j, and having i transactions already
    # max_local[i][j] is to store the maximum profit at day j, having i transactions already, and having transaction at day j
    max_global = [[0] * length for _ in xrange(k + 1)]
    max_local = [[0] * length for _ in xrange(k + 1)]

    # i indicates the transaction times, j indicates the times
    for j in xrange(1, length):
        cur_profit = prices[j] - prices[j - 1]  # variable introduced by the current day transaction
        for i in xrange(1, k + 1):
            # max_global depends on max_local, so updata local first, and then global.
            max_local[i][j] = max(max_global[i - 1][j - 1] + max(cur_profit, 0), max_local[i][j - 1] + cur_profit)
            # if cur_profit <0, then the current transaction loses money, so max_local[i][j] = max_global[i-1][j-1]
            # else, it can be max_global[i-1][j-1] + cur_profit, by considering the current transaction
            # or it can be max_local[i][j-1] + cur_profit, this is to CANCEL the last day transaction and moves to the current transaction. Note this doesn't change the total number of transactions. Also, max_local[i-1] has already been considered by max_global[i-1] term
            max_global[i][j] = max(max_global[i][j - 1], max_local[i][j])
            # This is more obvious, by looking at whether transaction on day j has influenced max_global or not.
    return max_global[k][-1]  # the last day, the last transaction