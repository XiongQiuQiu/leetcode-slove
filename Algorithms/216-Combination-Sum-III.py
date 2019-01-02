'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''



def combinationSum3(k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    ans = []

    def dfs(ans, stack, target, l,s):
        for i in range(s, 10):
            if target == 0 and l == 0:
                ans.append(stack[:])
                return
            if target-i < 0 or l-1 < 0:
                return
            dfs(ans, stack+[i], target - i, l - 1,i+1)
    dfs(ans, [], n, k,1)
    return ans
print combinationSum3(3,7)