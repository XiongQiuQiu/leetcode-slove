
def quicksort(nums,l,r):
    if l< r:
        q = partition(nums,l,r)
        quicksort(nums,l,q-1)
        quicksort(nums,q+1,r)
    return nums

def partition(nums,l,r):
    low = l
    while l < r:
        if nums[l] < nums[r]:
            nums[l],nums[low] = nums[low],nums[l]
            low += 1
        l += 1
    nums[low],nums[r]=nums[r],nums[low]
    return low
nums = [6,3,5,9,1,7,4]
print quicksort(nums,0,len(nums)-1)
