#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (38.63%)
# Total Accepted:    67.2K
# Total Submissions: 174K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# 
# 
# Note: Do not use any built-in library function such as sqrt.
# 
# 
# Example 1:
# 
# Input: 16
# Returns: True
# 
# 
# 
# Example 2:
# 
# Input: 14
# Returns: False
# 
# 
# 
# Credits:Special thanks to @elmirap for adding this problem and creating all
# test cases.
#
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l,r = 1, num/2
        while l +1 < r:
            mid = l + (r-l) / 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                l = mid
            else:
                r = mid
        return True if l * l == num  or r * r == num else False
