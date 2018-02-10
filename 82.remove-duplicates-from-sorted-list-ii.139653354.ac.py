#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (29.87%)
# Total Accepted:    127.7K
# Total Submissions: 427.4K
# Testcase Example:  '[]'
#
# 
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
# 
# 
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        prev = dummy
        curr = head
        prev.next = curr
        while curr:
            while curr.next and curr.val == curr.next.val: ## continue move to next node
                curr = curr.next
            if prev.next != curr:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return dummy.next
        
