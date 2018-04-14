#
# [658] Find K Closest Elements
#
# https://leetcode.com/problems/find-k-closest-elements/description/
#
# algorithms
# Medium (34.96%)
# Total Accepted:    16.1K
# Total Submissions: 46K
# Testcase Example:  '[1,2,3,4,5]\n4\n3'
#
# 
# Given a sorted array, two integers k and x, find the k closest elements to x
# in the array.  The result should also be sorted in ascending order.
# If there is a tie,  the smaller elements are always preferred.
# 
# 
# Example 1:
# 
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]
# 
# 
# 
# 
# Example 2:
# 
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]
# 
# 
# 
# Note:
# 
# The value k is positive and will always be smaller than the length of the
# sorted array.
# ⁠Length of the given array is positive and will not exceed 104
# ⁠Absolute value of elements in the array and x will not exceed 104
# 
# 
# 
# 
# 
# 
# UPDATE (2017/9/19):
# The arr parameter had been changed to an array of integers (instead of a list
# of integers). Please reload the code definition to get the latest changes.
# 
#
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        l, r = 0, len(arr)-1
        while l + 1 < r:
            mid = l + (r-l)/2
            if arr[mid] == x:
                l = mid
                break
            elif arr[mid] < x:
                l = mid
            else:
                r = mid
        if arr[l] == x:
            start = l
        elif arr[r] == x:
            start = r
        else:
            if arr[r] - x < x - arr[l]:
                start = l
            else:
                start = r
                
        end = start
        while end - start < k:
            if start == 0:
                return arr[:k]
            elif end == len(arr):
                return arr[-k:]
            if x - arr[start-1] <= arr[end] - x:
                start-= 1
            else:
                end += 1
        return arr[start:end]
        
