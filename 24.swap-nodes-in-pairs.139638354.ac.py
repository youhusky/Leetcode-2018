#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (38.96%)
# Total Accepted:    201.2K
# Total Submissions: 516.4K
# Testcase Example:  '[]'
#
# 
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# 
# 
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# 
# 
# Your algorithm should use only constant space. You may not modify the values
# in the list, only nodes itself can be changed.
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        curr = dummy
        curr.next = head
        while curr.next and curr.next.next:
            # store 1st, 2nd node
            first = curr.next
            second = curr.next.next
            # point nodes
            first.next = second.next
            curr.next = second
            # reverse node
            curr.next.next = first
            # move to the new head
            curr = curr.next.next
        return dummy.next
