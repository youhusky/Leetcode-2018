#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Easy (39.84%)
# Total Accepted:    185K
# Total Submissions: 464.2K
# Testcase Example:  '[]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Credits:Special thanks to @ifanchu for adding this problem and creating all
# test cases. Also thanks to @ts for adding additional test cases.
#
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        
        first = nums[0]
        second = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            third = max(first + nums[i], second)
            first = second
            second = third
        return second
        
