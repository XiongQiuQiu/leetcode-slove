def maxProduct(nums):
    maximum=big=small=nums[0]
    for n in nums[1:]:
        big, small=max(n, n*big, n*small), min(n, n*big, n*small)
        maximum=max(maximum, big)
    return maximum

maxProduct([-2,3,-2,-4])
# maxProduct([2,3,-2,4])