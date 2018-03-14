#
# [151] Reverse Words in a String
#
# https://leetcode.com/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (15.64%)
# Total Accepted:    190.6K
# Total Submissions: 1.2M
# Testcase Example:  '""'
#
# 
# Given an input string, reverse the string word by word.
# 
# 
# 
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
# 
# 
# 
# Update (2015-02-12):
# For C programmers: Try to solve it in-place in O(1) space.
# 
# 
# click to show clarification.
# 
# Clarification:
# 
# 
# 
# What constitutes a word?
# A sequence of non-space characters constitutes a word.
# Could the input string contain leading or trailing spaces?
# Yes. However, your reversed string should not contain leading or trailing
# spaces.
# How about multiple spaces between two words?
# Reduce them to a single space in the reversed string.
# 
# 
# 
#
class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])
