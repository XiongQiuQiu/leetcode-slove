'''

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.



Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000

'''


class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        event = []
        odd = []
        for num in A:
            if num % 2:
                odd.append(num)
            else:
                event.append(num)
        event.extend(odd)
        return event


class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        start, end = 0, len(A) - 1
        while start < end:
            m, n = A[start], A[end]
            if m % 2 == 1 and n % 2 == 0:
                A[start], A[end] = n, m
            elif m % 2 == 1:
                end -= 1
            elif n % 2 == 0:
                start += 1
            else:
                start += 1
                end -= 1
        return A
