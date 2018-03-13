#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (40.04%)
# Total Accepted:    240.3K
# Total Submissions: 600.1K
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
# 
# You may assume no duplicates in the array.
# 
# Example 1:
# 
# Input: [1,3,5,6], 5
# Output: 2
# 
# 
# 
# Example 2:
# 
# Input: [1,3,5,6], 2
# Output: 1
# 
# 
# 
# Example 3:
# 
# Input: [1,3,5,6], 7
# Output: 4
# 
# 
# 
# Example 1:
# 
# Input: [1,3,5,6], 0
# Output: 0
# 
# 
#
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l +1 < r:
            mid =  l + (r - l)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid
            else:
                r = mid
                
        # find
        if nums[l] >= target:
            return l
        elif nums[r] >= target:
            return r
        else:
            return r+1
        
        
