#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (33.40%)
# Total Accepted:    99.1K
# Total Submissions: 296.8K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string str, find if str follows the same pattern.
# ⁠Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
# 
# Examples:
# 
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# 
# 
# 
# 
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters separated by a single space.
# 
# 
# Credits:Special thanks to @minglotus6 for adding this problem and creating
# all test cases.
#
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dic = dict()
        strlist = str.split(" ")
        if len(pattern) != len(strlist):
            return False
        dic1 = dict()
        dic2 = dict()
        
        for i,value in enumerate(pattern):
            dic1[value] = dic1.get(value,[]) + [i]
        for i,value in enumerate(strlist):
            dic2[value] = dic2.get(value, []) + [i]
            
        return sorted(dic1.values()) == sorted(dic2.values())
        
