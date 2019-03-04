'''
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
'''


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sums = sum(nums)
        if sums & 1: return False
        nset = set([0])
        for num in nums:
            for num2 in nset.copy():
                nset.add(num + num2)
        return sums / 2 in nset


class Solution(object):
    def canFindSum(self, nums, target, ind, n, d):
        if target in d: return d[target]
        if target == 0:
            d[target] = True
        else:
            d[target] = False
            if target > 0:
                for i in xrange(ind, n):
                    if self.canFindSum(nums, target - nums[i], i + 1, n, d):
                        d[target] = True
                        break
        return d[target]

    def canPartition(self, nums):
        s = sum(nums)
        if s % 2 != 0: return False
        return self.canFindSum(nums, s / 2, 0, len(nums), {})

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        dp = [True] + [False] * (total / 2)
        for i in xrange(1, len(nums) + 1):
            for j in reversed(xrange(1, total / 2 + 1)):
                dp[j] = dp[j] or (j - nums[i - 1] >= 0 and dp[j - nums[i - 1]])
        return dp[-1] and not total % 2
