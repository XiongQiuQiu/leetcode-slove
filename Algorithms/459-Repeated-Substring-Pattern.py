'''
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.



Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

'''

'''
Basic idea:

First char of input string is first char of repeated substring
Last char of input string is last char of repeated substring
Let S1 = S + S (where S in input string)
Remove 1 and last char of S1. Let this be S2
If S exists in S2 then return true else false
Let i be index in S2 where S starts then repeated substring length i + 1 and repeated substring S[0: i+1]
'''

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not str: return False
        ss = (s + s)[1:-1]
        return ss.find(s) != -1

'''
I would try to propose a more strict proof idea:
It's obvious that valid string will be captured by this algorithm, but why invalid one return false is not intuitive.
From the algorithm, we can conclude that S satisfies that s = AB = BA (by AB, I mean s = the concatenation of A and B).
What I want to prove is if AB = BA, then there is a D such that A = n*D, B = m*D
Suppose len(A) = a, len(B) = b. Two cases:

If a = b or a = 1 or b = 1, the problem is trivial.
Without loss of generality, we could suppose that a < b.
According to AB = BA, we have A = B[1~a], which means that B = AC.
Then AB = BA ==> AAC = ACA and the problem size has been reduced from (a, b) to (a-b, b): AC = CA.
In the end, it will be reduced to one of the case in (1). Thus the problem is solved.'''