#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (36.33%)
# Total Accepted:    19.3K
# Total Submissions: 53.1K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, write a function to return true if s2 contains
# the permutation of s1. In other words, one of the first string's permutations
# is the substring of the second string.
# 
# Example 1:
# 
# Input:s1 = "ab" s2 = "eidbaooo"
# Output:True
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# 
# 
# Example 2:
# 
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
# 
# 
# 
# Note:
# 
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].
# 
# 
#
class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # O(n)
        dic1, dic2 = dict(), dict()
        for s in s1:
            dic1[s] = dic1.get(s,0) + 1
        start, end = 0, 0
        
        while end < len(s2):
            dic2[s2[end]] = dic2.get(s2[end],0) + 1
            if dic1 == dic2:
                return True
            
            end += 1
            
            # compare
            if end -start + 1 > len(s1):
                dic2[s2[start]] -= 1
                if dic2[s2[start]] == 0:
                    del(dic2[s2[start]])
                start += 1
        return False
