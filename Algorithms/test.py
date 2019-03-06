def findTargetSumWays(nums, S):
    """
    :type nums: List[int]
    :type S: int
    :rtype: int
    """
    sums = sum(nums)
    if sums < S or (sums + S) & 1 == 1: return 0
    dp = [1] + [0] * ((sums + S) / 2)
    for num in nums:
        for i in range(len(dp))[::-1]:
            dp[i] = dp[i] + (i >= num and dp[i - num])
    return dp[-1]
findTargetSumWays([1,1,1,1,1],3)