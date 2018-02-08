# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy1, dummy2 = ListNode(0), ListNode(0)
        curr1 = dummy1
        curr2 = dummy2
        # seperate into two parts
        while head:
            if head.val < x:
                curr1.next = head
                curr1 = head
            else:
                curr2.next = head
                curr2 = head
            head = head.next
            
        # set last
        curr2.next = None
        curr1.next = dummy2.next
        return dummy1.next
        
        
