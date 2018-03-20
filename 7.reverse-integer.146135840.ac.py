#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (24.37%)
# Total Accepted:    381.7K
# Total Submissions: 1.6M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# Input: 123
# Output:  321
# 
# 
# 
# Example 2:
# 
# Input: -123
# Output: -321
# 
# 
# 
# Example 3:
# 
# Input: 120
# Output: 21
# 
# 
# 
# Note:
# Assume we are dealing with an environment which could only hold integers
# within the 32-bit signed integer range. For the purpose of this problem,
# assume that your function returns 0 when the reversed integer overflows.
# 
#
class Solution:
    # @return an integer
    def reverse(self, x):
        result = 0

        if x < 0:
            symbol = -1
            x = -x
        else:
            symbol = 1

        while x:
            result = result * 10 + x % 10
            x /= 10

        return 0 if result > pow(2, 31) else result * symbol
