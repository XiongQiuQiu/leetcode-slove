'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = []
        def dfs(s,tmp, stack, ans):
            if tmp:
                stack.append(tmp)
            if not s:
                ans.append(stack)
            for i in range(len(s)):
                if s[:i+1] == s[:i+1][::-1] :
                    dfs(s[i + 1:],s[:i+1], stack[:], ans)
        dfs(s,'', [], ans)
        return ans