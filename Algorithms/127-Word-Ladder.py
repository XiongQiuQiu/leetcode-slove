'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        word_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '_' + word[i + 1:]
                word_dict[key].append(word)
        queue = collections.deque([[beginWord, 1]])
        vistied = set([beginWord])
        while queue:
            word, length = queue.popleft()
            if self.wordcnt(word, endWord) == 0:
                return length
            for i in range(len(word)):
                key = word[:i] + '_' + word[i + 1:]
                for token in word_dict[key]:
                    if token not in vistied:
                        vistied.add(token)
                        queue.append([token, length + 1])
        return 0

    def wordcnt(self, wordA, wordB):
        return sum([wordA[i] != wordB[i] for i in range(len(wordA))])

