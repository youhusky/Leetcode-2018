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
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        curr = dummy
        curr.next = head
        while curr.next and curr.next.next:
            # store 1st, 2nd node
            first = curr.next
            second = curr.next.next
            # point nodes
            first.next = second.next
            curr.next = second
            # reverse node
            curr.next.next = first
            # move to the new head
            curr = curr.next.next
        return dummy.next
