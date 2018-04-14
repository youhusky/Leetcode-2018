#
# [524] Longest Word in Dictionary through Deleting
#
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/
#
# algorithms
# Medium (43.25%)
# Total Accepted:    21.3K
# Total Submissions: 49.3K
# Testcase Example:  '"abpcplea"\n["ale","apple","monkey","plea"]'
#
# 
# Given a string and a string dictionary, find the longest string in the
# dictionary that can be formed by deleting some characters of the given
# string. If there are more than one possible results, return the longest word
# with the smallest lexicographical order. If there is no possible result,
# return the empty string.
# 
# Example 1:
# 
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
# 
# Output: 
# "apple"
# 
# 
# 
# 
# Example 2:
# 
# Input:
# s = "abpcplea", d = ["a","b","c"]
# 
# Output: 
# "a"
# 
# 
# 
# Note:
# 
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.
# 
# 
#
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        res = ""
        for word in d:
            if self.check(s, word):
                if len(word) > len(res) or len(word) == len(res) and word[0] < res[0]:
                    res = word
        return res
        
    def check(self, word1, word2):
        # word2 shorter
        i,j = 0,0
        while i < len(word1) and j < len(word2):
            if word1[i] == word2[j]:
                j += 1
            i += 1
        return j == len(word2)
        
