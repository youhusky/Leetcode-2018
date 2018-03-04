#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (33.85%)
# Total Accepted:    189.3K
# Total Submissions: 559.3K
# Testcase Example:  '"0"\n"0"'
#
# 
# Given two binary strings, return their sum (also a binary string).
# 
# 
# 
# For example,
# a = "11"
# b = "1"
# Return "100".
# 
#
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        res = ""
        carry = 0
        while i >= 0 or j >= 0:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            res = str(carry%2) + res
            carry /= 2
        return res if not carry else "1" + res
        
