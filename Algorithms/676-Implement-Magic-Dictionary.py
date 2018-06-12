class MagicDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = collections.defaultdict(set)

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for string in dict:
            for i in range(len(string)):
                word = string[:i] + '_' + string[i + 1:]
                self.dict[word].add(string[i])

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for i in range(len(word)):
            letter = word[:i] + '_' + word[i + 1:]
            values = self.dict[letter]
            if not values: continue
            if len(values) > 1 or word[i] not in self.dict[letter]: return True
        return False



        # Your MagicDictionary object will be instantiated and called as such:
        # obj = MagicDictionary()
        # obj.buildDict(dict)
        # param_2 = obj.search(word)