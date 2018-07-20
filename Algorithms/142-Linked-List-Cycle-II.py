'''

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        num = 0
        while fast and fast.next:
            if num == 0:
                slow, fast = slow.next, fast.next.next
                if slow == fast:
                    num = 1
            if num == 1:
                if slow == head:
                    return head
                slow, head = slow.next, head.next

        return None


