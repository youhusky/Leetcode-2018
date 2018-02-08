# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode

        for i in range(m - 1):
            pre = pre.next
        
        # reverse the [m, n] nodes
        prev = None
        cur = pre.next
        for i in range(n - m + 1):
            p = cur.next
            cur.next = prev
            prev = cur
            cur = p
        # link 2-5, 1-4
        pre.next.next = cur
        pre.next = prev

        return dummyNode.next
        
