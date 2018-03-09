#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (37.99%)
# Total Accepted:    186.9K
# Total Submissions: 492.1K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# 
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
# Return:
# 
# [
# ⁠ ["ate", "eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note: All inputs will be in lower-case.
#
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = dict()
        for w in strs:
            word = w
            w = str(sorted(w))
            if w not in dic:
                dic[w] = [word]
            else:
                dic[w].append(word)
        return dic.values()
        
