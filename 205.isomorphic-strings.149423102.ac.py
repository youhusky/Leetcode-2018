#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (34.60%)
# Total Accepted:    130.3K
# Total Submissions: 376.5K
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
# 
# For example,
# Given "egg", "add", return true.
# 
# Given "foo", "bar", return false.
# 
# Given "paper", "title", return true.
# 
# Note:
# You may assume both s and t have the same length.
#
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # O (nlgn)
        # corner case
        if len(s) != len(t):
            return False
        dic1 = dict()
        dic2 = dict()
        
        for i,value in enumerate(s):
            dic1[value] = dic1.get(value,[]) + [i]
        for i,value in enumerate(t):
            dic2[value] = dic2.get(value, []) + [i]
            
        return sorted(dic1.values()) == sorted(dic2.values())
        
