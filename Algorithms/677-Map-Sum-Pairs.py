class TrieNode(object):
    def __init__(self):
        self.children = dict()
        self.val = 0
        self.sum = 0


class MapSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        node = self.root
        nodes = []
        for k in key:
            child = node.children.get(k)
            if child is None:
                child = TrieNode()
                node.children[k] = child
            nodes.append(child)
            node = child
        if node.val != val:
            delta = val - node.val
            node.val = val
            for node in nodes:
                node.sum += delta

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        for k in prefix:
            node = node.children.get(k)
            if node is None: return 0
        return node.sum


        # Your MapSum object will be instantiated and called as such:
        # obj = MapSum()
        # obj.insert(key,val)
        # param_2 = obj.sum(prefix)