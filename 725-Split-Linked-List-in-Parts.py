# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def countlen(self, root):
        n = 0
        while root:
            n += 1
            root = root.next
        return n

    def initans(self, l, k):
        perlen = l / k
        mod = l % k
        ans = []
        n = 0
        for i in range(k):
            if i < mod:
                t = 1
            else:
                t = 0
            ans.append(perlen + t)
        return ans

    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        l = self.countlen(root)
        num = self.initans(l, k)
        ans = []
        for one in num:
            if one is 0:
                ans.append(None)
                continue
            node = root
            for i in range(one-1):
                node = node.next
            ans.append(root)
            root = node.next
            node.next = None
        return ans



