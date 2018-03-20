#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (33.36%)
# Total Accepted:    144.2K
# Total Submissions: 432.3K
# Testcase Example:  '[]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
#
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
        
