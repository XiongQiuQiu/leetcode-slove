'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
'''
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n<2: return 0
        if k>=n/2:
            return sum(i-j for i,j in zip(prices[1:], prices[:-1]) if i-j>0)
        maxglobal = [[0] * n for _ in range(k+1)]
        for i in range(1,k+1):
            maxlocal = [0] * n
            for j in range(1,n):
                profit = prices[j] - prices[j-1]
                maxlocal[j] =max(
                maxglobal[i-1][j-1]+max(profit,0),
                maxlocal[j-1]+profit)
                maxglobal[i][j] = max(maxglobal[i][j-1],maxlocal[j])
        return maxglobal[k][-1]

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        earn = 0
        if k >= len(prices) // 2:  # loot every increase
            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    earn += prices[i] - prices[i - 1]
            return earn

        dp = [0 for _ in prices]
        for i in range(k):
            pre_max = dp[0] - prices[0]
            for j in range(1, len(prices)):
                dp[j], pre_max = max(dp[j - 1], prices[j] + pre_max), max(pre_max, dp[j] - prices[j])
        return dp[-1]