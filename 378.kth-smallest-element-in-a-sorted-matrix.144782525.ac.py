#
# [378] Kth Smallest Element in a Sorted Matrix
#
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (45.49%)
# Total Accepted:    56.4K
# Total Submissions: 123.9K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# Given a n x n matrix where each of the rows and columns are sorted in
# ascending order, find the kth smallest element in the matrix.
# 
# 
# Note that it is the kth smallest element in the sorted order, not the kth
# distinct element.
# 
# 
# Example:
# 
# matrix = [
# ⁠  [ 1,  5,  9],
# ⁠  [10, 11, 13],
# ⁠  [12, 13, 15]
# ],
# k = 8,
# 
# return 13.
# 
# 
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ n2.
#
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # O(klgk)
        pq = []
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        heapq.heappush(pq,(matrix[0][0],0,0))
        # two ways
        while k:
            result, i, j = heapq.heappop(pq)
            if i+1 < m:
                heapq.heappush(pq, (matrix[i+1][j], i+1, j))
            # only first row need to go right
            if j+1 < n and i == 0:
                # go down
                heapq.heappush(pq, (matrix[i][j+1], i, j+1))
            k -= 1
        return result
            
