#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (35.42%)
# Total Accepted:    116.8K
# Total Submissions: 329.6K
# Testcase Example:  '"aab"'
#
# 
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# 
# Return all possible palindrome partitioning of s.
# 
# 
# For example, given s = "aab",
# 
# Return
# 
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
# 
#
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPal(s[:i]):
                # rest string
                self.dfs(s[i:], path+[s[:i]], res)

    def isPal(self, s):
        return s == s[::-1]
