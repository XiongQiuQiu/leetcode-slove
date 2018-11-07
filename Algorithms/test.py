def rotateRight(self,k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    l = 1 if head else 0
    while head and head.next:
        head = head.next
        l + 1
    dummpy = ListNode(None)
    dummpy.next = head
    cur = head
    end = 1
    while cur and cur.next:
        if end == l - k:
            new_start = cur.next
            while new_start and new_start.next:
                new_start = new_start.next
            new_start.next = cur
            dummpy.next = new_start
            return dummpy.next
        cur = cur.next
        end += 1