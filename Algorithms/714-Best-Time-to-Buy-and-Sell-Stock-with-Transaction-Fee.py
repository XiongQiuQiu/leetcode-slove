'''
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
'''

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        dp = [ [0,0] for _ in range(len(prices)) ]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1,len(prices)):
            dp[i][1] = max(dp[i-1][0]-prices[i],dp[i-1][1])
            dp[i][0] = max(dp[i-1][1] + prices[i]-fee,dp[i-1][0])
        return dp[-1][0]



class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        stack = [[50000, 0]]
        for price in prices:
            if not stack[-1][1] and price <= stack[-1][0]:
                stack[-1][0] = price
            elif price >= max(stack[-1][0] + fee, stack[-1][1]):
                stack[-1][1] = price
            elif stack[-1][1]:
                stack.append([price, 0])
            while len(stack) > 1 and stack[-2][1] < stack[-1][0] + fee:
                stack[-1][1] = max(stack.pop()[1], stack[-1][1])
        return sum(t[1] - t[0] - fee for t in stack if t[1] - t[0] > fee)

        hold, sell = -prices[0], 0
        for p in prices:
            hold = max(sell - p, hold)
            sell = max(hold + p - fee, sell)
        return sell

