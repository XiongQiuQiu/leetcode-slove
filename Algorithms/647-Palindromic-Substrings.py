'''
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.
'''


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        queue = collections.deque((i, i) for i in range(size))
        for i in range(size - 1):
            if s[i] == s[i + 1]:
                queue.append((i, i + 1))
        ans = 0
        while queue:
            x, y = queue.popleft()
            ans += 1
            if x - 1 >= 0 and y + 1 < size and s[x - 1] == s[y + 1]:
                queue.append((x - 1, y + 1))
        return ans
