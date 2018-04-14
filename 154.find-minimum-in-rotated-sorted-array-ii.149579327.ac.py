#
# [154] Find Minimum in Rotated Sorted Array II
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (37.85%)
# Total Accepted:    95.1K
# Total Submissions: 251.1K
# Testcase Example:  '[1]'
#
# 
# Follow up for "Find Minimum in Rotated Sorted Array":
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
# Find the minimum element.
# 
# The array may contain duplicates.
#
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l, r = 0 ,len(nums)-1
        if nums[l] < nums[r]:
            return nums[l]
        while l + 1 < r:
            mid = l + (r-l)/2
            if nums[mid] == nums[r]:
                r -= 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                l = mid
        return min(nums[l], nums[r])
        
