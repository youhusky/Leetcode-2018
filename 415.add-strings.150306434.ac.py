#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings/description/
#
# algorithms
# Easy (41.74%)
# Total Accepted:    55.9K
# Total Submissions: 133.8K
# Testcase Example:  '"0"\n"0"'
#
# Given two non-negative integers num1 and num2 represented as string, return
# the sum of num1 and num2.
# 
# Note:
# 
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#
class Solution(object):
    def addStrings(self, nums1, nums2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # 123 + 
        #  45
        
        res = ""
        i,j = len(nums1)-1, len(nums2)-1
        carry =  0
        while i >= 0 or j >= 0 :
            if i >= 0:
                carry += int(nums1[i])
                i -= 1
            if j >= 0:
                carry += int(nums2[j])
                j -= 1
            res = str(carry%10) + res
            carry /= 10
        return res if not carry else '1' + res
