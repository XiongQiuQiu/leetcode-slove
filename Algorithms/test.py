def wiggleMaxLength( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    size = len(nums)
    dp = [1] * size
    status = [0] * size
    for x in range(size):
        for y in range(x):
            if (status[y] == 1 and nums[x] > nums[y]) or (status[y] == -1 and nums[x] < nums[y]) or (status ==0 and nums[x] != nums[y]):
                status[x] = [-1, 1][dp[x] > dp[y] + 1] * status[y]
                dp[x] = max(dp[x], dp[y] + 1)
    return max(dp) if dp else 0


wiggleMaxLength([1,7,4,9,2,5])