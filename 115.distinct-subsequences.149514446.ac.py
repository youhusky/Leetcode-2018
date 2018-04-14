#
# [115] Distinct Subsequences
#
# https://leetcode.com/problems/distinct-subsequences/description/
#
# algorithms
# Hard (32.19%)
# Total Accepted:    82.4K
# Total Submissions: 255.9K
# Testcase Example:  '"rabbbit"\n"rabbit"'
#
# Given a string S and a string T, count the number of distinct subsequences of
# S which equals T.
# 
# A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (ie, "ACE" is a
# subsequence of "ABCDE" while "AEC" is not).
# 
# Here is an example:
# S = "rabbbit", T = "rabbit"
# 
# Return 3.
# 
#
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]
        for j in range(len(s)+1):
            dp[0][j] = 1
            
        for i in range(len(t)):
            for j in range(len(s)):
                
                if s[j] == t[i]:
                    dp[i+1][j+1] = dp[i][j] + dp[i+1][j]
                else:
                    dp[i+1][j+1] = dp[i+1][j]
        
        return dp[-1][-1]
