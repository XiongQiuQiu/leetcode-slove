'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.



Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummpy = ListNode(None)
        dummpy.next = head
        pre = dummpy
        while head and head.next:
            n = head.next
            c = head
            pre.next = head.next
            tmp = head.next.next
            head.next.next = head
            c.next = tmp
            pre = pre.next.next
            head = tmp
        return dummpy.next