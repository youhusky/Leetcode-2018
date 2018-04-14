#
# [632] Smallest Range
#
# https://leetcode.com/problems/smallest-range/description/
#
# algorithms
# Hard (41.94%)
# Total Accepted:    9.1K
# Total Submissions: 21.7K
# Testcase Example:  '[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]'
#
# You have k lists of sorted integers in ascending order. Find the smallest
# range that includes at least one number from each of the k lists. 
# 
# We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c
# if b-a == d-c.
# 
# Example 1:
# 
# Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# Output: [20,24]
# Explanation: 
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
# 
# 
# 
# 
# Note:
# 
# The given list may contain duplicates, so ascending order means >= here.
# 1 k 
# ⁠-105 value of elements 5.
# For Java users, please note that the input type has been changed to
# List<List<Integer>>. And after you reset the code template, you'll see this
# point.
# 
# 
# 
#
import heapq
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # nlgk
        pq = []
        max_val = nums[0][0]
        for i in range(len(nums)):
            heapq.heappush(pq,(nums[i][0],i,0))
            max_val = max(max_val, nums[i][0])
            
        min_range = [float('-inf'), float('inf')]
        while pq:
            min_val, i, j = heapq.heappop(pq)
            # condition
            if max_val - min_val < min_range[1] - min_range[0] or max_val - min_val == min_range[1] - min_range[0] and min_val < min_range[0]:
                min_range = [min_val, max_val]
            if j < len(nums[i]) - 1:
                heapq.heappush(pq, (nums[i][j+1], i, j+1))
                max_val = max(max_val, nums[i][j+1])
            else:
                return min_range
            
        
