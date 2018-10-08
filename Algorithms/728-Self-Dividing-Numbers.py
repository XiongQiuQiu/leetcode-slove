'''

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input:
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.
'''
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for d in range(left,right+1):
            dstr = str(d)
            for i in range(len(dstr)):
                if int(dstr[i]) != 0 and d % int(dstr[i]) ==0:
                    if i == len(dstr) -1:
                        ans.append(d)
                else:
                    break
        return ans


class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def check(num):
            digits = set(map(int, str(num)))
            if 0 in digits: return False
            return not any(num % d for d in digits)
        return filter(check, range(left, right + 1))