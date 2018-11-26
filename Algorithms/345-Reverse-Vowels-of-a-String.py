'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
'''
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return s
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        ans = list(s)
        i,j=0,len(s)-1
        while i < j:
            if ans[i] not in vowel:
                i += 1
            if ans[j] not in vowel:
                j -= 1
            if ans[i] in vowel and ans[j] in vowel:
                ans[i],ans[j]=ans[j],ans[i]
                i +=1
                j -= 1
        return ''.join(ans)