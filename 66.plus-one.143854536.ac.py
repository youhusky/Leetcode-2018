#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (39.60%)
# Total Accepted:    225.7K
# Total Submissions: 569.9K
# Testcase Example:  '[0]'
#
# Given a non-negative integer represented as a non-empty array of digits, plus
# one to the integer.
# 
# You may assume the integer do not contain any leading zero, except the number
# 0 itself.
# 
# The digits are stored such that the most significant digit is at the head of
# the list.
#
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # O(n)
        carry = 1
        for i in range(len(digits)-1, -1,-1):
            digits[i] = (digits[i] + 1) % 10
            if digits[i]:
                carry = 0
                break
        if carry:
            digits.insert(0,1)
        return digits
        
