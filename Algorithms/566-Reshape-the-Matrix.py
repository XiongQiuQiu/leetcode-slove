class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        allnum = []
        ans = []
        for x in nums:
            allnum.extend(x)
        if r * c != len(allnum):
            return nums
        else:
            for i in range(r):
                ans.append(allnum[i * c:c * (i + 1)])
        return ans
