#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (32.51%)
# Total Accepted:    113.4K
# Total Submissions: 348.9K
# Testcase Example:  '""\n""'
#
# 
# Given two words word1 and word2, find the minimum number of steps required to
# convert word1 to word2. (each operation is counted as 1 step.)
# 
# 
# 
# You have the following 3 operations permitted on a word:
# 
# 
# 
# a) Insert a character
# b) Delete a character
# c) Replace a character
# 
#
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # We define the state dp[i][j] to be the minimum number of operations to convert word1[0..i - 1] to word2[0..j - 1]
        l1 = len(word1)+1
        l2 = len(word2) + 1
        dp = [[0 for _ in range(l2)] for _ in range(l1)]
        
        for i in range(l1):
            dp[i][0] = i
        for j in range(l2):
            dp[0][j] = j
        for i in range(1,l1):
            for j in range(1,l2):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j], dp[i-1][j-1]) + 1
        #print dp
        return dp[-1][-1]
