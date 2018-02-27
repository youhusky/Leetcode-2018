#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (37.73%)
# Total Accepted:    102.7K
# Total Submissions: 272.1K
# Testcase Example:  '1'
#
# 
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# 
# 
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13,
# return 2 because 13 = 4 + 9.
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [n+2] * (n+1)
        for i in range(1,n+1):
            
            if i*i > n:
                break
            else:
                
                dp[i*i] = 1
        
        for i in range(1, n+1):
            for j in range(1,n+1):
                if i + j*j > n:
                    break
                else:
                    dp[i + j*j] = min(dp[i] + 1, dp[i + j*j])
        return dp[n]
