'''

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


'''
def maxSubArray(self, nums):
    for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1: return nums[0]
        cursum = [nums[0]] + [-20000] * len(nums)
        maxsum = nums[0]
        for i in range(1, len(nums)):
            cursum[i] = max(nums[i], cursum[i - 1] + nums[i])
            maxsum = max(maxsum, cursum[i])
        return maxsum

