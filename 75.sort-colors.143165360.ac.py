#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (38.81%)
# Total Accepted:    209.8K
# Total Submissions: 540.6K
# Testcase Example:  '[0]'
#
# 
# Given an array with n objects colored red, white or blue, sort them so that
# objects of the same color are adjacent, with the colors in the order red,
# white and blue.
# 
# 
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white,
# and blue respectively.
# 
# 
# 
# Note:
# You are not suppose to use the library's sort function for this problem.
# 
# 
# click to show follow up.
# 
# 
# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting
# sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
# array with total number of 0's, then 1's and followed by 2's.
# Could you come up with an one-pass algorithm using only constant space?
# 
# 
#
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red, blue = 0 ,len(nums)-1
        i = 0
        # i == blue means we still need to compute whether there is a change
        while i <= blue:
            if nums[i] == 0:
                nums[i], nums[red] = nums[red], nums[i]
                i += 1
                red += 1
            elif nums[i] == 2:
                nums[i], nums[blue] = nums[blue], nums[i]
                blue -= 1
            else:
                i += 1
            
