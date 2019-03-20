'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        i,j=0,len(s)-1
        while i<j:
            if s[i] != s[j]:
                return self.isvalid(s,i,j-1) or self.isvalid(s,i+1,j)
            i += 1
            j -= 1
        return True
    def isvalid(self,s,i,j):
        while i<j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True