#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (36.85%)
# Total Accepted:    112.1K
# Total Submissions: 304.1K
# Testcase Example:  '0'
#
# Given an integer n, return the number of trailing zeroes in n!.
# 
# Note: Your solution should be in logarithmic time complexity.
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            n /= 5
            count += n
        return count
