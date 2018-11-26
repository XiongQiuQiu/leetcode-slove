'''
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False
'''


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        sqrt = int(math.sqrt(c))
        for i in range(sqrt + 1):
            b = c - i ** 2
            if int(math.sqrt(b)) ** 2 + i ** 2 == c: return True
        return False

def slove(self,c):
    i=0
    j=math.sqrt(c)
    while i<=j:
        powsum =i**2 + j**2
        if c ==powsum:
            return True
        elif powsum < c:
            i +=1
        else:
            j -=1
    return False