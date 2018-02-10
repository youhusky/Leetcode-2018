#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (24.42%)
# Total Accepted:    129.9K
# Total Submissions: 532.1K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a list, rotate the list to the right by k places, where k is
# non-negative.
# 
# 
# 
# Example:
# 
# Given 1->2->3->4->5->NULL and k = 2,
# 
# return 4->5->1->2->3->NULL.
# 
# 
#
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
        
        
        
