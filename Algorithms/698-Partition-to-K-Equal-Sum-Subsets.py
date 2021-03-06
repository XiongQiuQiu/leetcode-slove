'''

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
'''
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k ==1: return True
        n = len(nums)
        if k > n: return False
        total = sum(nums)
        if total % k : return False
        target = total/k
        visit = [0] * n
        nums.sort(reverse=True)
        def dfs(k,ind,sums):
            if k == 1: return True
            if sums == target:
                return dfs(k-1,0,0)
            for i in range(ind,n):
                if not visit[i] and sums + nums[i] <=target:
                    visit[i] = 1
                    if dfs(k,i+1,sums+nums[i]):
                        return True
                    visit[i] = 0
            return False
        return dfs(k,0,0)