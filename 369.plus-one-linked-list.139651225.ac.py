# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
            
        node = ListNode(0)
        val = 1
        while stack:
            val += stack.pop()
            node.val = val%10
            carry = ListNode(val/10)
            carry.next = node
            node = carry
            val /= 10
        return node.next if node.val == 0 else node # node - 1
            
        
