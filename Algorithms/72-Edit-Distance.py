'''Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')'''
# O(m*n) space
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1,l2 = len(word1),len(word2)
        dp = [ [0]*(l2+1) for _ in range(l1+1)]
        for i in range(1,l2+1):
            dp[0][i] = dp[0][i-1] + 1
        for i in range(1,l1+1):
            dp[i][0] = dp[i-1][0] + 1
            for j in range(1,l2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        return dp[l1][l2]

# O(n) space with rolling array
def minDistance(self, word1, word2):
    l1, l2 = len(word1) + 1, len(word2) + 1
    pre = [0 for _ in xrange(l2)]
    for j in xrange(l2):
        pre[j] = j
    for i in xrange(1, l1):
        cur = [i] * l2
        for j in xrange(1, l2):
            cur[j] = min(cur[j - 1] + 1, pre[j] + 1, pre[j - 1] + (word1[i - 1] != word2[j - 1]))
        pre = cur[:]
    return pre[-1]