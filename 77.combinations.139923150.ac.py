#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (40.85%)
# Total Accepted:    136.3K
# Total Submissions: 333.7K
# Testcase Example:  '4\n2'
#
# 
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
# 
# 
# For example,
# If n = 4 and k = 2, a solution is:
# 
# 
# 
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
#
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # O(2^n)
        res = []
        self.backtracking(n,k,res,[], 1)
        return res
    def backtracking(self,n,k,res,temp,start):
        if k == 0:
            res.append(list(temp))
        for i in range(start, n+1):
            temp.append(i)
            self.backtracking(n,k-1,res,temp,i+1)
            temp.pop()
        
