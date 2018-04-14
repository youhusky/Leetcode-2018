#
# [357] Count Numbers with Unique Digits
#
# https://leetcode.com/problems/count-numbers-with-unique-digits/description/
#
# algorithms
# Medium (46.08%)
# Total Accepted:    46.4K
# Total Submissions: 100.8K
# Testcase Example:  '2'
#
# Given a non-negative integer n, count all numbers with unique digits, x,
# where 0 ≤ x < 10n.
# 
# 
# ⁠   Example:
# Given n = 2, return 91. (The answer should be the total numbers in the range
# of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])
# 
# 
# Credits:Special thanks to @memoryless for adding this problem and creating
# all test cases.
#
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans, product = 1, 1
        
        for i in range (min(n,10)):
            product *= choices[i]
            ans += product
            
        return ans
