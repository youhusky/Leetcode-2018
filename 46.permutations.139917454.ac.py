#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (46.43%)
# Total Accepted:    216.2K
# Total Submissions: 465.4K
# Testcase Example:  '[1,2,3]'
#
# 
# Given a collection of distinct numbers, return all possible permutations.
# 
# 
# 
# For example,
# [1,2,3] have the following permutations:
# 
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.backtracking(nums, [], res)
        return res
    def backtracking(self, nums, temp, ans):
        if len(nums) == len(temp): # quit loop
            ans.append(list(temp))
        for i in range(len(nums)):
            if nums[i] in temp: # cut duplicate
                continue
            temp.append(nums[i])
            
            self.backtracking(nums, temp, ans)
            temp.pop()

