#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (31.21%)
# Total Accepted:    131.2K
# Total Submissions: 420.5K
# Testcase Example:  '[5]\n1\n1'
#
# 
# Reverse a linked list from position m to n. Do it in-place and in
# one-pass.
# 
# 
# 
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
# 
# 
# return 1->4->3->2->5->NULL.
# 
# 
# Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list.
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode

        for i in range(m - 1):
            pre = pre.next
        
        # reverse the [m, n] nodes
        prev = None
        cur = pre.next
        for i in range(n - m + 1):
            p = cur.next
            cur.next = prev
            prev = cur
            cur = p
        # link 2-5, 1-4
        pre.next.next = cur
        pre.next = prev

        return dummyNode.next
        
