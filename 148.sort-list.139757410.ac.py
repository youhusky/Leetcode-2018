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
        prev,fast, slow =  None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        prev.next = None ## cut the middle
        
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        
        return self.merge(l1, l2)
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        # check rest
        if l1:
            curr.next = l1
        else:
            curr.next = l2
        return dummy.next
        
