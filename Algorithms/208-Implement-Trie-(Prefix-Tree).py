'''

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''


class Trie(object):
    class Node(object):
        def __init__(self, val):
            self.val = val
            self.children = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tries = {}
        self.words = set()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.tries.get(word[0])
        if not node:
            node = Trie.Node(word[0])
            self.tries[word[0]] = node
        head = node
        for s in word[1:]:
            if s not in node.children:
                node.children[s] = Trie.Node(s)
            node = node.children[s]
        self.words.add(word)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return word in self.words

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.tries.get(prefix[0])
        if not node: return False
        for s in prefix[1:]:
            if s not in node.children:
                return False
            node = node.children[s]
        return True




        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)