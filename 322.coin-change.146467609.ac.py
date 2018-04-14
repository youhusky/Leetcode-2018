#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (26.60%)
# Total Accepted:    86.4K
# Total Submissions: 324.6K
# Testcase Example:  '[1]\n0'
#
# 
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
# 
# 
# 
# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
# 
# 
# 
# Example 2:
# coins = [2], amount = 3
# return -1.
# 
# 
# 
# Note:
# You may assume that you have an infinite number of each kind of coin.
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        maxnumber = amount + 1
        dp = [maxnumber] * ((amount) + 1)
        dp[0] = 0
        for i in range(1,amount+1):
            for j in range(len(coins)):
                if i >= coins[j] :
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        return dp[-1] if not dp[-1] == maxnumber else -1
        
