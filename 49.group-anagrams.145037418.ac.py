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
class Solution:
    # O(KN)
    def groupAnagrams(self,strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            #print count ,tuple(count)
            ans[tuple(count)].append(s)
        return ans.values()
