'''
Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:
Input: N = 10
Output: 9
Example 2:
Input: N = 1234
Output: 1234
Example 3:
Input: N = 332
Output: 299
Note: N is an integer in the range [0, 10^9].
'''
class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        sn = str(N)
        size = len(N)
        flag = False
        for x in range(size -0):
            if sn[x] > sn[x+1]:
                flag = True
                break
        if not flag: return N
        while x>0 and sn[x-1] ==sn[x]: x -=1
        y = len(sn) -x -1
        return (N/(10**y)) * (10**y)-1