'''

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

'''
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dfs(queens,dif,sum_):
            p = len(queens)
            if p == n:
                result.append(queens)
            for q in range(n):
                if q not in queens and p-q not in dif and q+p not in sum_:
                    dfs(queens+[q],dif+[p-q],sum_+[p+q])
        result = []
        dfs([],[],[])
        return len(result)