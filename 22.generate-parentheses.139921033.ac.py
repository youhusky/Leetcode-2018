#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (47.29%)
# Total Accepted:    192.5K
# Total Submissions: 406.9K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n < 1:
            return []
        res = []
        self.backtracking(n, res, "", 0, 0)
        return res
    def backtracking(self,n, res, temp, left, right):
        if left < n:
            self.backtracking(n, res, temp + '(' , left+1, right)
        if right < left:
            self.backtracking(n ,res, temp + ')', left, right+1)
        if right == n:
            res.append(temp)
        
