# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        prev = dummy
        curr = head
        prev.next = curr
        while curr:
            while curr.next and curr.val == curr.next.val: ## continue move to next node
                curr = curr.next
            if prev.next != curr:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return dummy.next
        
