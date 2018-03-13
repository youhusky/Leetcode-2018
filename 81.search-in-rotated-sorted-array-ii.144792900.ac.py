#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (32.72%)
# Total Accepted:    115.4K
# Total Submissions: 352.7K
# Testcase Example:  '[]\n5'
#
# 
# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
# 
# Would this affect the run-time complexity? How and why?
# 
# 
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# Write a function to determine if a given target is in the array.
# 
# The array may contain duplicates.
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return False
        l, r = 0, len(nums)-1
        # == not near mid because already find the condition one 
        while l + 1 < r:
            mid = l + (r-l) /2
            if nums[mid] == target:
                return True
            
            # before pivot
            if nums[mid] > nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid
            # after pivot
            elif nums[mid] < nums[l]:
                if nums[mid] < target <= nums[r]:
                    l = mid
                else:
                    r = mid
            else:
                l += 1
        # corner case
        if nums[l] == target:
            return True
        if nums[r] == target:
            return True
        return False
                    
