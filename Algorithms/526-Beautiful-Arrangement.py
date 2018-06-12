class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        cache = dict()
        def slove(idx, nums):
            if not nums: return 1
            key = idx, tuple(nums)
            if key in cache: return cache[key]
            ans = 0
            for i, n in enumerate(nums):
                if n % idx == 0 or idx % n == 0:
                    ans += slove(idx + 1, nums[:i] + nums[i+1:])
            cache[key] = ans
            return ans
        return slove(1, range(1, N + 1))