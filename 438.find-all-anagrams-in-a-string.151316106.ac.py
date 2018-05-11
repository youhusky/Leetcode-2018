#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Easy (33.90%)
# Total Accepted:    59.7K
# Total Submissions: 176.1K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given a string s and a non-empty string p, find all the start indices of p's
# anagrams in s.
# 
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
# 
# The order of output does not matter.
# 
# Example 1:
# 
# Input:
# s: "cbaebabacd" p: "abc"
# 
# Output:
# [0, 6]
# 
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# 
# Example 2:
# 
# Input:
# s: "abab" p: "ab"
# 
# Output:
# [0, 1, 2]
# 
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# 
#
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        dic1, dic2 = dict(), dict()
        for each in p:
            dic1[each] = dic1.get(each,0) + 1
        start, end = 0, 0
        res = []
        
        while end < len(s):
            dic2[s[end]] = dic2.get(s[end],0) + 1
            if dic1 == dic2:
                res.append(start)
            
            end += 1
                
            # compare
            if end -start + 1 > len(p):
                dic2[s[start]] -= 1
                if dic2[s[start]] == 0:
                    del(dic2[s[start]])
                start += 1
        return res

