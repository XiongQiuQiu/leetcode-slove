class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        firstbuy,firstsell = -float('inf'),0
        secondbuy,secondsell = -float('inf'),0
        for price in prices:
            if firstbuy < -price:
                firstbuy = -price
            if firstsell < firstbuy + price:
                firstsell = firstbuy + price
            if secondbuy < firstsell -price:
                secondbuy  = firstsell -price
            if secondsell < secondbuy + price:
                secondsell = secondbuy+ price
        return secondsell