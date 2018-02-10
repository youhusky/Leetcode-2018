#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (33.31%)
# Total Accepted:    117.3K
# Total Submissions: 352.1K
# Testcase Example:  '[]\n0'
#
# Given a linked list and a value x, partition it such that all nodes less than
# x come before nodes greater than or equal to x.
# 
# 
# You should preserve the original relative order of the nodes in each of the
# two partitions.
# 
# 
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.
# 
#
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
        
        
