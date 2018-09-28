'''

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
'''
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        cnt =collections.Counter(S)
        ans = '#'
        while cnt:
            stop = True
            for s,n in cnt.most_common():
                if s != ans[-1] :
                    stop = False
                    cnt[s] -=1
                    ans += s
                    if cnt[s] ==0: del cnt[s]
                    break
            if stop == True: return ''
        return ans[1:]