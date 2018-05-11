#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (40.75%)
# Total Accepted:    186.9K
# Total Submissions: 458.7K
# Testcase Example:  '[1]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.
#
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0 ,len(nums)-1
        # init check
        if nums[l] < nums[r]:
            return nums[l]
        
        while l + 1 < r:
            mid = l + (r-l) /2
            # l always index to the larger one
            if nums[r] > nums[mid]:
                r = mid
            else:
                l = mid
        return min(nums[r], nums[l])
