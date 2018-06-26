'''
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''
class KeyNode(object):

    def __init__(self, key, value, freq=1):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = None
        self.next = None


class FreqNode(object):

    def __init__(self, freq, prev, next):
        self.freq = freq
        self.next = next
        self.prev = prev
        self.first = None
        self.last = None


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.keyDict = dict()
        self.freqDict = dict()
        self.head = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        entry = self.keyDict.get(key)
        if entry is not None:
            self.increase(entry.key, entry.value)
            return entry.value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return
        if key in self.keyDict:
            self.increase(key, value)
            return
        if len(self.keyDict) == self.capacity:
            self.removeKeyNode(self.head.last)
        self.insertKeyNode(key, value)

    def increase(self, key, value):
        keyNode = self.keyDict.get(key)
        keyNode.value = value
        freqNode = self.freqDict[keyNode.freq]
        nextFreqNode = freqNode.next
        keyNode.freq += 1
        if nextFreqNode is None or nextFreqNode.freq > keyNode.freq:
            nextFreqNode = self.insertFreqNodeAfter(keyNode.freq, freqNode)
        self.unlinkKey(keyNode, freqNode)
        self.linkKey(keyNode, nextFreqNode)

    def insertKeyNode(self, key, value):
        keynode = self.keyDict[key] = KeyNode(key, value)
        freqNode = self.freqDict.get(1)
        if freqNode is None:
            freqNode = self.freqDict[1] = FreqNode(1, None, self.head)
            if self.head:
                self.head.prev = freqNode
            self.head = freqNode
        self.linkKey(keynode, freqNode)

    def delFreqNode(self, freqnode):
        prev, next = freqnode.prev, freqnode.next
        if prev: prev.next = next
        if next: next.prev = prev
        if self.head == freqnode: self.head = next
        del self.freqDict[freqnode.freq]

    def insertFreqNodeAfter(self, freq, freqNode):
        newNode = FreqNode(freq, freqNode, freqNode.next)
        self.freqDict[freq] = newNode
        if freqNode.next: freqNode.next.prev = newNode
        freqNode.next = newNode
        return newNode

    def removeKeyNode(self, keyNode):
        self.unlinkKey(keyNode, self.freqDict[keyNode.freq])
        del self.keyDict[keyNode.key]

    def unlinkKey(self, keyNode, freqNode):
        next, prev = keyNode.next, keyNode.prev
        if prev: prev.next = next
        if next: next.prev = prev
        if freqNode.first == keyNode: freqNode.first = keyNode.next
        if freqNode.last == keyNode: freqNode.last = keyNode.prev
        if freqNode.first is None: self.delFreqNode(freqNode)

    def linkKey(self, keyNode, freqNode):
        firstKeyNode = freqNode.first
        keyNode.prev = None
        keyNode.next = firstKeyNode
        if firstKeyNode: firstKeyNode.prev = keyNode
        freqNode.first = keyNode
        if freqNode.last is None: freqNode.last = keyNode

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)