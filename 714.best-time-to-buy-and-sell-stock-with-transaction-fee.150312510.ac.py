#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
#
# algorithms
# Medium (45.64%)
# Total Accepted:    15K
# Total Submissions: 32.9K
# Testcase Example:  '[1,3,2,8,4,9]\n2'
#
# Your are given an array of integers prices, for which the i-th element is the
# price of a given stock on day i; and a non-negative integer fee representing
# a transaction fee.
# You may complete as many transactions as you like, but you need to pay the
# transaction fee for each transaction.  You may not buy more than 1 share of a
# stock at a time (ie. you must sell the stock share before you buy again.)
# Return the maximum profit you can make.
# 
# Example 1:
# 
# Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# Buying at prices[0] = 1Selling at prices[3] = 8Buying at prices[4] = 4Selling
# at prices[5] = 9The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# 
# 
# 
# Note:
# 0 < prices.length .
# 0 < prices[i] < 50000.
# 0 .
# 
#
class Solution(object):
    def maxProfit(self, prices, fee):
    	# only consider the buy and sell
        N = len(prices)
        if not N:
            return 0
        
        sell = 0
        buy = -prices[0]
        for i in range(1, N):
            buy = max(buy, sell - prices[i])
            sell = max(sell, buy + prices[i] - fee)
        return max(sell, 0)

