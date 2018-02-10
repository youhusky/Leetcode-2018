#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (28.01%)
# Total Accepted:    201.3K
# Total Submissions: 718.8K
# Testcase Example:  '[]'
#
# 
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq = []
        dummy = ListNode(0)
        head = dummy
        for node in lists:
            # check node exist
            if node:
                heapq.heappush(pq,(node.val, node))
                
        while pq:
            head.next = heapq.heappop(pq)[1]
            head = head.next
            # head.next in this list still exist
            if head.next:
                heapq.heappush(pq,(head.next.val, head.next))
        return dummy.next
        
