'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        letter_num = set(list(string.letters)) | set([str(num) for num in range(10)])
        use_letter = []
        for letter in s.lower():
            if letter in letter_num:
                use_letter.append(letter)
        return use_letter == list(reversed(use_letter))
