#
# [34] Search for a Range
#
# https://leetcode.com/problems/search-for-a-range/description/
#
# algorithms
# Medium (31.59%)
# Total Accepted:    180.5K
# Total Submissions: 571.3K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers sorted in ascending order, find the starting and
# ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# 
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].
# 
#
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    #O (lgN)
    # search first occers
    def searchRange(self, A, target):
        if len(A) == 0:
            return [-1, -1]
        
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        
        if A[start] == target:
            leftBound = start
        elif A[end] == target:
            leftBound = end
        else:
            return [-1, -1]
        
        # search last occers
        start, end = leftBound, len(A) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        if A[end] == target:
            rightBound = end
        else:
            rightBound = start
        return [leftBound, rightBound]
