'''
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
#
# '''


class Node(object):

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dummpyNode = Node(-1, -1)
        self.tail = self.dummpyNode
        self.size = 0
        self.entryFinder = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        entry = self.entryFinder.get(key)
        if entry == None:
            return -1
        else:
            val = entry.val
            self.renew(entry)
            return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        entry = self.entryFinder.get(key)
        if entry is None:
            entry = Node(key, value)
            self.entryFinder[key] = entry
            self.tail.next = entry
            entry.prev = self.tail
            self.tail = entry
            if self.size < self.capacity:
                self.size += 1
            else:
                headNode = self.dummpyNode.next
                if headNode is not None:
                    self.dummpyNode.next = headNode.next
                    headNode.next.prev = self.dummpyNode
                del self.entryFinder[headNode.key]

        else:
            entry.val = value
            self.renew(entry)

    def renew(self, entry):
        if self.tail != entry:
            nextNode = entry.next
            prevNode = entry.prev
            prevNode.next = nextNode
            nextNode.prev = prevNode
            self.tail.next = entry
            entry.prev = self.tail
            entry.next = None
            self.tail = entry

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)