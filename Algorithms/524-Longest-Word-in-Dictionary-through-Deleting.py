'''
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
'''
import collections
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        ans = []
        dmap = collections.defaultdict(list)
        for w in d:
            dmap[w[0]].append((0, w))
        for string in s:
            wlist = dmap[string]
            del dmap[string]
            for i,w in wlist:
                if i +1 == len(w):
                    ans.append(w)
                else:
                    dmap[w[i+1]].append((i+1,w))
        if not ans: return ''
        maxl = len(max(ans,key=len))
        return min(w for w in ans if len(w) == maxl)
def findLongestWord(self, S, D):
    D.sort(key = lambda x: (-len(x), x))
    for word in D:
        i = 0
        for c in S:
            if i < len(word) and word[i] == c:
                i += 1
        if i == len(word):
            return word
    return ""