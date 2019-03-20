'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        ll = []
        i = 1
        while i*i <= n:
            ll.append(i*i)
            i += 1
        ans =0
        check = {n}
        while check:
            tmp = set()
            ans += 1
            for y in check:
                for x in ll:
                    if x == y:
                        return ans
                    elif x>y:
                        break
                    tmp.add(y-x)
            check = tmp