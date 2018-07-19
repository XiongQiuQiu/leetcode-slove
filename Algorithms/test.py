
def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    size = len(nums)
    i = -1
    end = size
    while i < end:
        i += 1
        if nums[i] == 0:
            del nums[i]
            nums.insert(0, 0)
        if nums[i] == 2:
            del nums[i]
            nums.insert(size, 2)
            i -= 1
            end -=1
        print(nums)


sortColors([2,0,2,1,1,0])