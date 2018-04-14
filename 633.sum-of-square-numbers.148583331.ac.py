#
# [633] Sum of Square Numbers
#
# https://leetcode.com/problems/sum-of-square-numbers/description/
#
# algorithms
# Easy (32.30%)
# Total Accepted:    22.7K
# Total Submissions: 70.2K
# Testcase Example:  '5'
#
# 
# Given a non-negative integer c, your task is to decide whether there're two
# integers a and b such that a2 + b2 = c.
# 
# 
# Example 1:
# 
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
# 
# 
# 
# 
# Example 2:
# 
# Input: 3
# Output: False
# 
# 
# 
#
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        l,r = 0, int(math.sqrt(c))
        while l <= r:
            mid = l*l + r*r
            if mid < c:
                l += 1
            elif mid > c:
                r -= 1
            else:
                return True
        return False
        
