#
# [316] Remove Duplicate Letters
#
# https://leetcode.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Hard (30.36%)
# Total Accepted:    39.3K
# Total Submissions: 129.4K
# Testcase Example:  '"bcabc"'
#
# 
# Given a string which contains only lowercase letters, remove duplicate
# letters so that every letter appear once and only once. You must make sure
# your result is the smallest in lexicographical order among all possible
# results.
# 
# 
# 
# Example:
# 
# 
# Given "bcabc"
# Return "abc"
# 
# 
# Given "cbacdcbc"
# Return "acdb"
# 
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        dic = dict()
        for char in s:
            dic[char] = dic.get(char, 0) + 1
            
        for char in s:
            dic[char] -= 1
            if char in stack:
                continue
            else:
                while stack and ord(char) < ord(stack[-1]) and dic[stack[-1]] > 0:
                    stack.pop()
            stack.append(char)
        return "".join(stack)
