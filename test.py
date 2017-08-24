def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    xor = reduce(lambda x, y: x ^ y, nums)
    print 'xor',xor
    lowbit = xor & -xor
    print 'lowbit', lowbit
    a = b = 0
    for num in nums:
        print '&', num & lowbit
        if num & lowbit:
            a ^= num
            print 'a',a
        else:
            b ^= num
            print 'b', b
        print '------------'
    return [a, b]
nums=[1, 2, 1, 3, 2, 5]
print singleNumber(nums)
print '---------'
nums=[1, 2, 1, 3, 2, 5]
for i in nums:
    print i & 2