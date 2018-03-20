#
# [13] Roman to Integer
#
# https://leetcode.com/problems/roman-to-integer/description/
#
# algorithms
# Easy (47.87%)
# Total Accepted:    217.6K
# Total Submissions: 454.7K
# Testcase Example:  '"DCXXI"'
#
# Given a roman numeral, convert it to an integer.
# 
# Input is guaranteed to be within the range from 1 to 3999.
#
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10,'V': 5,'I': 1}
        prev, res = 0, 0
        for i in range(len(s)-1, -1,-1):
            curr = romans[s[i]]
            if curr >= prev:
                res += curr
            else:
                res -= curr
            prev = curr
        return res
        
