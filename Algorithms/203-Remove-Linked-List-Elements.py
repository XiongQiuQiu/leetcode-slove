'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        first = ListNode(None)
        first.next = head
        pre = first
        while head:
            if head.val == val:
                pre.next = head.next
                head.next = None
                head = pre.next
            else:
                pre = head
                head = head.next
        return first.next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummpy = ListNode(None)
        dummpy.next = head
        next = dummpy
        while next != None and next.next != None:
            if next.next.val == val:
                next.next = next.next.next
            else:
                next = next.next
        return dummpy.next
