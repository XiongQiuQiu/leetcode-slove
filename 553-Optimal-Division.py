class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        return '/'.join(str(i) for i in nums) if len(nums) <= 3 else str(nums[0]) + '/(' + '/'.join(
            str(i) for i in nums[1:]) + ')'

