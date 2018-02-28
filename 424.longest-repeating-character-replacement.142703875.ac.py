#
# [424] Longest Repeating Character Replacement
#
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (42.70%)
# Total Accepted:    17.4K
# Total Submissions: 40.7K
# Testcase Example:  '"ABAB"\n2'
#
# Given a string that consists of only uppercase English letters, you can
# replace any letter in the string with another letter at most k times. Find
# the length of a longest substring containing all repeating letters you can
# get after performing the above operations.
# 
# Note:
# Both the string's length and k will not exceed 104.
# 
# 
# 
# Example 1:
# 
# Input:
# s = "ABAB", k = 2
# 
# Output:
# 4
# 
# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
# 
# 
# 
# 
# Example 2:
# 
# Input:
# s = "AABABBA", k = 1
# 
# Output:
# 4
# 
# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# 
# 
#
from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dic = defaultdict(int)
        res = 0
        start = 0
        for i in range(len(s)):
            dic[s[i]] += 1
            res = max(res, dic[s[i]])
            if res + k <= i - start:
                dic[s[start]] -= 1
                start += 1
                
        return len(s) - start
        
