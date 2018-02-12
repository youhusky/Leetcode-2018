#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (43.76%)
# Total Accepted:    215.2K
# Total Submissions: 491.5K
# Testcase Example:  '[1,2,3]'
#
# 
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# 
# For example,
# If nums = [1,2,3], a solution is:
# 
# 
# 
# [
# ⁠ [3],
# ⁠ [1],
# ⁠ [2],
# ⁠ [1,2,3],
# ⁠ [1,3],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ []
# ]
# 
#
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # O(2^n)
        res = []
        self.backtracking(nums, res, [],0)
        return res
    
    def backtracking(self, nums, res, temp,start):
        res.append(list(temp))
        for i in range(start, len(nums)):
            temp.append(nums[i])
            self.backtracking(nums, res, temp, i+1)
            temp.pop()
