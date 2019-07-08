'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        l, r = 0, len(nums) - 1
        if nums[l] == target: return l
        if nums[r] == target: return r

        while l + 1 < r:
            mid = (l + r) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[r]:
                if nums[mid] < target and target <= nums[r]:
                    l = mid
                else:
                    r = mid
            if nums[mid] >= nums[l]:
                if nums[mid] > target and target >= nums[l]:
                    r = mid
                else:
                    l = mid
        return -1


