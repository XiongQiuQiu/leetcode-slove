'''

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        mid, slow, fast = None, head, head
        while fast and fast.next:
            mid, slow, fast = slow, slow.next, fast.next.next
        mid.next = None
        return self.merge(*map(self.sortList, (head, slow)))

    def merge(self, lhead, rhead):
        dummpyNode = ListNode(None)
        dummpyhead = dummpyNode
        while lhead and rhead:
            if lhead.val < rhead.val:
                dummpyhead.next = lhead
                lhead = lhead.next
            else:
                dummpyhead.next = rhead
                rhead = rhead.next
            dummpyhead = dummpyhead.next
        dummpyhead.next = lhead or rhead
        return dummpyNode.next
