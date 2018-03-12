#
# [214] Shortest Palindrome
#
# https://leetcode.com/problems/shortest-palindrome/description/
#
# algorithms
# Hard (25.10%)
# Total Accepted:    51.2K
# Total Submissions: 203.8K
# Testcase Example:  '"aacecaaa"'
#
# 
# Given a string S, you are allowed to convert it to a palindrome by adding
# characters in front of it. Find and return the shortest palindrome you can
# find by performing this transformation.
# 
# 
# For example: 
# Given "aacecaaa", return "aaacecaaa".
# Given "abcd", return "dcbabcd".
# 
# Credits:Special thanks to @ifanchu for adding this problem and creating all
# test cases. Thanks to @Freezen for additional test cases.
#
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev = s[::-1]
        j = 0
        for i in range(len(s)):
            if s[:len(s) - i] == rev[i:]:
                return rev[:i] + s
        return ""
        
