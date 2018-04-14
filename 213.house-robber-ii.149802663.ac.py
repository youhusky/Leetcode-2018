#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (34.61%)
# Total Accepted:    75K
# Total Submissions: 216.7K
# Testcase Example:  '[]'
#
# Note: This is an extension of House Robber.
# 
# After robbing those houses on that street, the thief has found himself a new
# place for his thievery so that he will not get too much attention. This time,
# all houses at this place are arranged in a circle. That means the first house
# is the neighbor of the last one. Meanwhile, the security system for these
# houses remain the same as for those in the previous street. 
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Credits:Special thanks to @Freezen for adding this problem and creating all
# test cases.
#
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        if len(nums) < 2:
            return nums[0]
        return max(self.rob_helper(nums,0,len(nums)-1), self.rob_helper(nums, 1, len(nums)))
    
    def rob_helper(self, nums, start, end):
        if start == 0:
            first = nums[0]
            second = max(nums[0], nums[1])
        else:
            first = 0
            second = nums[1]
        for i in range(2, end):
            third = max(first + nums[i], second)
            first = second
            second = third
        return second
            
                   
            
        
