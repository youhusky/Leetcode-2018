class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        # split
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1, head2 = head, slow.next
        slow.next = None
        # reverse
        cur, pre = head2, None
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        # merge
        cur1, cur2 = head1, pre
        while cur2:
            nex1, nex2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = nex1
            cur1, cur2 = nex1, nex2
