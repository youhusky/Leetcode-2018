#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (26.90%)
# Total Accepted:    211.6K
# Total Submissions: 786.5K
# Testcase Example:  '""'
#
# 
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# 
# 
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
# 
# 
# 
# Note:
# Have you consider that the string might be empty? This is a good question to
# ask during an interview.
# 
# For the purpose of this problem, we define empty string as valid palindrome.
# 
#
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
