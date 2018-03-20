#
# [26] Remove Duplicates from Sorted Array
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
#
# algorithms
# Easy (36.13%)
# Total Accepted:    325K
# Total Submissions: 899.4K
# Testcase Example:  '[1,1,2]'
#
# 
# Given a sorted array, remove the duplicates in-place such that each element
# appear only once and return the new length.
# 
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
# 
# 
# Example:
# 
# Given nums = [1,1,2],
# 
# Your function should return length = 2, with the first two elements of nums
# being 1 and 2 respectively.
# It doesn't matter what you leave beyond the new length.
# 
# 
#
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # like move zero
        if len(nums) < 1:
            return 0
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[count] = nums[i]
                count += 1
        return count
        
