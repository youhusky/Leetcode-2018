# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        length = 1
        p = head
        while p.next:
            p = p.next
            length += 1
        
        # link to the head
        p.next = head
        move = length - k % length
        while  move > 1:
            head = head.next
            move -= 1
            
        newHead = head.next
        head.next = None
        
        return newHead
        
        
        
