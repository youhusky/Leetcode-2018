# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        # check mid point
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        newHead = slow
        prev = None
        curr = newHead
        while curr:
            p = curr.next
            curr.next = prev
            prev = curr
            curr = p
        # prev -> new Head
        
        while prev and head:
            print prev.val, head.val
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
        
