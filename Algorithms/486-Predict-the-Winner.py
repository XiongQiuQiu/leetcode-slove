'''
Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Example 1:
Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2.
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2).
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
Hence, player 1 will never be the winner and you need to return False.
Example 2:
Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
Note:
1 <= length of the array <= 20.
Any scores in the given array are non-negative integers and will not exceed 10,000,000.
If the scores of both players are equal, then player 1 is still the winner.
'''


class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cache = dict()

        def solve(nums):
            if len(nums) <= 1: return sum(nums)
            tnums = tuple(nums)
            if tnums in cache: return cache[tnums]
            cache[tnums] = max(nums[0] - solve(nums[1:]), nums[-1] - solve(nums[:-1]))
            return cache[tnums]

        return solve(nums) >= 0


class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) % 2 == 0 or len(nums) == 1:
            return True

        n = len(nums)
        dp = [[[0, 0] for row in xrange(n)] for _ in xrange(n)]

        # bottom up, build each case starting from problem with 1 number in a game:
        # base case: only 1 number, player 1 pick first, player 2 will be left with 0 number game, aka 0
        # each dp[i][j] will store [bestScore, leftOver]
        for i in range(n):
            dp[i][i] = [nums[i], 0]

        # sub divide the game into list from index i to j
        # now start from 2 number game [i][j]:
        # if player 1 pick i, player 2 will pick the bestScore of game [i+1][j], then player 1 is left with the leftOver of game [i+1][j]
        # if player 1 pick j, player 2 will pick the bestScore of game [i][j-1], then player 1 is left with the leftOver of game [i][j-1]
        # player 1 will choose the best case in above scenarios

        for length in xrange(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # pick i:
                pi = dp[i + 1][j][1] + nums[i]
                # pick j:
                pj = dp[i][j - 1][1] + nums[j]
                if pi > pj:
                    dp[i][j][0] = pi
                    dp[i][j][1] = dp[i + 1][j][0]

                else:
                    dp[i][j][0] = pj
                    dp[i][j][1] = dp[i][j - 1][0]

        return dp[0][-1][0] >= dp[0][-1][1]