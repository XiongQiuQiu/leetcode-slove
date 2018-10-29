'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
'''


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [-1] * amount
        for i in range(amount):
            if dp[i] < 0:
                continue
            for coin in coins:
                if i + coin > amount:
                    continue
                if dp[i + coin] < 0 or dp[i + coin] > dp[i] + 1:
                    dp[i + coin] = dp[i] + 1
        return dp[-1]
