#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (31.59%)
# Total Accepted:    256.9K
# Total Submissions: 813.2K
# Testcase Example:  '[]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
#
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs: return ''
        first = min(strs)
        for i in range(len(first)):
            for s in strs:
                if s[i] != first[i]:
                    return first[:i] if i > 0 else ''
        return first
