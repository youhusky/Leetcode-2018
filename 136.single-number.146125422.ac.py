#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (55.24%)
# Total Accepted:    278.8K
# Total Submissions: 504.6K
# Testcase Example:  '[1]'
#
# Given an array of integers, every element appears twice except for one. Find
# that single one.
# 
# 
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
#
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
        return res
