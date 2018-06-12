class TrieNode(object):
    def __init__(self):
        self.children = dict()
        self.isword = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string):
        node = self.root
        for k in string:
            child = node.children.get(k)
            if not child:
                child = TrieNode()
                node.children[k] = child
            node = child
        node.isword = True

    def search(self, string):
        ans = ''
        node = self.root
        for i in string:
            node = node.children.get(i)
            if not node: break
            ans += i
            if node.isword == True: return ans
        return string


class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for word in dict: trie.insert(word)
        sentence = sentence.split()
        ans = []
        for word in sentence:
            ans.append(trie.search(word))
        return ' '.join(ans)
