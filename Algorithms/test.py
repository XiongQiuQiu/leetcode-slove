
def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    size = len(nums)
    dp = [1] * size
    for x in range(size):
        for y in range(x):
            if nums[x] > nums[y]:
                dp[x] = max(dp[x],dp[y]+1)
    return max(dp) if dp else 0

lengthOfLIS([10,9,2,5,3,7,101,18])
def lenght(nums):
    size = len(nums)
    dp = [1] * size
    for x in range(size):
        for y in range(x):
            if nums[x] > nums[y]:
                dp[x] = max(dp[x] ,dp[y]+1)
    return max(dp) if dp else 0

def lengthOfLIS1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    size = len(nums)
    dp = []
    for x in range(size):
        print
        low, high = 0, len(dp) - 1
        while low <= high:
            mid = (low + high) / 2
            if dp[mid] >= nums[x]:
                high = mid - 1
            else:
                low = mid + 1
        if low >= len(dp):
            dp.append(nums[x])
        else:
            dp[low] = nums[x]
    return len(dp)