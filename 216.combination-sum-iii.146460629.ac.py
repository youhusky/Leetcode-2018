#
# [216] Combination Sum III
#
# https://leetcode.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (47.12%)
# Total Accepted:    86.9K
# Total Submissions: 184.4K
# Testcase Example:  '3\n7'
#
# 
# Find all possible combinations of k numbers that add up to a number n, given
# that only numbers from 1 to 9 can be used and each combination should be a
# unique set of numbers.
# 
# 
# 
# ⁠Example 1:
# Input:  k = 3,  n = 7
# Output: 
# 
# [[1,2,4]]
# 
# 
# ⁠Example 2:
# Input:  k = 3,  n = 9
# Output: 
# 
# [[1,2,6], [1,3,5], [2,3,4]]
# 
# 
# 
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
#
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.backtracking(k,n,[],res,1)
        return res
    
    def backtracking(self, k, target, temp, res, start):
        if len(temp) > k:
            return
        elif len(temp) == k and target == 0:
            res.append(list(temp))
        else:
            for i in range(start, 10):
                temp.append(i)
                self.backtracking(k, target - i, temp, res, i+1)
                temp.pop()
        
        
