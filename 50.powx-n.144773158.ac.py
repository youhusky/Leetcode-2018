#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (26.03%)
# Total Accepted:    201.6K
# Total Submissions: 774.4K
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n).
# 
# 
# 
# 
# Example 1:
# 
# Input: 2.00000, 10
# Output: 1024.00000
# 
# 
# 
# Example 2:
# 
# Input: 2.10000, 3
# Output: 9.26100
# 
# 
#
class Solution:
    # @param {double} x the base number
    # @param {int} n the power number
    # @return {double} the result
    def myPow(self, x, n):
        # Write your code here
        if n < 0 :
            x = 1 / x
            n = -n

        ans = 1
        tmp = x

        while n != 0:
            if n % 2 == 1:
                ans *= tmp
            tmp *= tmp
            n /= 2
        return ans

