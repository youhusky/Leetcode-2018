#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (28.77%)
# Total Accepted:    216.5K
# Total Submissions: 752.3K
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x.
# 
# x is guaranteed to be a non-negative integer.
# 
# 
# 
# Example 1:
# 
# Input: 4
# Output: 2
# 
# 
# 
# Example 2:
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we want to return
# an integer, the decimal part will be truncated.
# 
# 
#
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        l, r = 1, x
        while l +1 < r:
            mid = l + (r-l)/2
            if mid*mid == x:
                return mid
            elif mid < x / mid:
                l = mid
            else:
                r = mid
        # find the right
        return r if r*r <= x else l
