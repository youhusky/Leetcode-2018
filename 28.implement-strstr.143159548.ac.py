#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (28.87%)
# Total Accepted:    252.1K
# Total Submissions: 873.2K
# Testcase Example:  '"hello"\n"ll"'
#
# 
# Implement strStr().
# 
# 
# 
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
# 
# 
# Example 1:
# 
# Input: haystack = "hello", needle = "ll"
# Output: 2
# 
# 
# 
# Example 2:
# 
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# 
# 
#
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        m = len(haystack) 
        n = len(needle) 
        for i in range(m):
            if i+n <= m:
                if haystack[i:i+n] == needle:
                    return i
        return -1
