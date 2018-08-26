'''

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
'''

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = list(str(num))
        numt = sorted(nums, reverse=True)
        for (i, n), m in zip(enumerate(nums), numt):
            if m == n: continue
            maxv = max(nums[i + 1:])
            j = nums[i + 1:][::-1].index(maxv) + 1
            nums[i], nums[-j] = nums[-j], nums[i]
            break
        return int(''.join(nums))

