#
# [122] Best Time to Buy and Sell Stock II
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
#
# algorithms
# Easy (47.77%)
# Total Accepted:    194.7K
# Total Submissions: 407.6K
# Testcase Example:  '[]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (ie, buy one and sell one share of the stock
# multiple times). However, you may not engage in multiple transactions at the
# same time (ie, you must sell the stock before you buy again).
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        n = len(prices)
        for i in range(n-1):
            if prices[i] < prices[i+1]:
                res += prices[i+1] - prices[i]
        return res
