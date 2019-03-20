'''

Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input:
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
Note:

All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].
'''
import collections
def numMatchingSubseq(S, words):
    waiting = collections.defaultdict(list)
    for w in words:
        waiting[w[0]].append(iter(w[1:]))
    for c in S:
        for it in waiting.pop(c, ()):
            waiting[next(it, None)].append(it)
    return len(waiting[None])
numMatchingSubseq("abcde",["a", "bb", "acd", "ace"])