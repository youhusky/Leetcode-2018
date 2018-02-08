# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1,stack2 = [],[]
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
            
        add_value = 0 # need to check
        node = ListNode(0)
        while stack1 or stack2:
            if stack1:
                add_value += stack1.pop()
            if stack2:
                add_value += stack2.pop()
            node.val = add_value % 10
            carry = ListNode(add_value / 10)
            carry.next = node
            node = carry
            add_value /= 10
        
        return node.next if node.val == 0 else node
            
        
