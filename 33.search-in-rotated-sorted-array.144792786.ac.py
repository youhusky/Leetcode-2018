#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (31.94%)
# Total Accepted:    241.2K
# Total Submissions: 754.9K
# Testcase Example:  '[]\n5'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        l, r = 0, len(nums)-1
        # == not near mid because already find the condition one 
        while l + 1 < r:
            mid = l + (r-l) /2
            if nums[mid] == target:
                return mid
            
            # before pivot
            if nums[mid] > nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid
            # after pivot
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid
                else:
                    r = mid
        # corner case
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1
                    
