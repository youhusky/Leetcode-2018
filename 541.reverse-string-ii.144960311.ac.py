#
# [541] Reverse String II
#
# https://leetcode.com/problems/reverse-string-ii/description/
#
# algorithms
# Easy (43.84%)
# Total Accepted:    34.9K
# Total Submissions: 79.6K
# Testcase Example:  '"abcdefg"\n2'
#
# 
# Given a string and an integer k, you need to reverse the first k characters
# for every 2k characters counting from the start of the string. If there are
# less than k characters left, reverse all of them. If there are less than 2k
# but greater than or equal to k characters, then reverse the first k
# characters and left the other as original.
# 
# 
# Example:
# 
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# 
# 
# 
# Restrictions: 
# 
# ⁠The string consists of lower English letters only.
# ⁠Length of the given string and k will in the range [1, 10000]
# 
#
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        length = len(s)
        # ba- cd fe
        for i in range(0, length, 2 * k):
            if i + k >= length:
                s = s[:i] + s[i:][::-1]
            else:
                s = s[:i] + s[i:i + k][::-1] + s[i + k:]
        return s
