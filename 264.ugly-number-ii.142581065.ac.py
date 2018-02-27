#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (33.26%)
# Total Accepted:    71.4K
# Total Submissions: 214.7K
# Testcase Example:  '1' 
#
# 
# Write a program to find the n-th ugly number.
# 
# 
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
# 
# 
# 
# Note that 1 is typically treated as an ugly number, and n does not exceed
# 1690.
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        i2, i3, i5 = 0,0,0
        while n:
            u2, u3, u5 = 2 *res[i2], 3*res[i3], 5*res[i5]
            temp = min(u2,u3,u5)
            if temp == u2:
                i2 += 1
            if temp == u3:
                i3 += 1
            if temp == u5:
                i5 += 1
            res.append(temp)
            n -= 1
        # dp[-2]
        return res[-2]
