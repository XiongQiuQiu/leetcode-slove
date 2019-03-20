class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        size = len(nums)
        status = None
        length = 1
        for x in range(1, size):
            if nums[x] > nums[x - 1] and status != True:
                status = True
                length += 1
            if nums[x] < nums[x - 1] and status != False:
                status = False
                length += 1
        return length
