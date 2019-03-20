class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        def dfs(ans, stack, nums):
            ans.append(stack[:])
            for i in range(len(nums)):
                if i >0 and nums[i]==nums[i-1]:
                    # dfs(ans, stack + [nums[i]],nums[i+1:])
                    pass
                else:
                    dfs(ans, stack + [nums[i]],nums[i + 1:])
        dfs(ans, [], nums)
        return ans
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        res = [[]]
        S.sort()
        for i in range(len(S)):
            if i == 0 or S[i] != S[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [S[i]])
        return res