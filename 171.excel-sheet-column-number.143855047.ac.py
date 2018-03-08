#
# [171] Excel Sheet Column Number
#
# https://leetcode.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (48.31%)
# Total Accepted:    160.4K
# Total Submissions: 331.9K
# Testcase Example:  '"A"'
#
# Related to question Excel Sheet Column Title
# Given a column title as appear in an Excel sheet, return its corresponding
# column number.
# 
# For example:
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28 
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution(object):
     def titleToNumber(self, s):
        key = 0
        l = len(s)
        count = 0
        if not s:
            return s
        else:
            for i in s:
                key += (ord(i)-64)*pow(26, l-1-count)
                count += 1
            return key
