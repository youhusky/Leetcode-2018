# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA = headA
        curB = headB
        l1, l2 = 0, 0
        while curA:
            curA = curA.next
            l1 += 1
        while curB:
            curB = curB.next
            l2 += 1
            
        if l1 < l2:
            for i in range(l2-l1):
                headB = headB.next
        else:
            for i in range(l1-l2):
                headA = headA.next
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
            
        
