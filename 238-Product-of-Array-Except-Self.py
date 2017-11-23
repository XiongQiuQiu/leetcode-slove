class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        output = [1] * size
        left = 1
        for i in range(size-1):
            left *= nums[i]
            output[i+1] *= left
        right = 1
        for i in range(size-1, 0, -1):
            right *= nums[i]
            output[i-1] *= right
        return output