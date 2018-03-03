#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (32.39%)
# Total Accepted:    22.7K
# Total Submissions: 69.9K
# Testcase Example:  '"aba"'
#
# 
# Given a non-empty string s, you may delete at most one character.  Judge
# whether you can make it a palindrome.
# 
# 
# Example 1:
# 
# Input: "aba"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# 
# 
# 
# Note:
# 
# The string will only contain lowercase characters a-z.
# The maximum length of the string is 50000.
# 
# 
#
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c1, c2 = 0,0
        l,r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                c1 += 1
                l += 1
            else:
                l += 1
                r -= 1
                
        l,r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                c2 += 1
                r -= 1
            else:
                l += 1
                r -= 1
                
        # because if either way is valid then should return True
        return c1 < 2 or c2 < 2
        
        
