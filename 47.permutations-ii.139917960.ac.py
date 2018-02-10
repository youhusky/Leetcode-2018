#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (34.53%)
# Total Accepted:    151.8K
# Total Submissions: 439.5K
# Testcase Example:  '[1,1,2]'
#
# 
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# 
# 
# For example,
# [1,1,2] have the following unique permutations:
# 
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        used = [False for _ in range(len(nums))]
        self.backtracking(nums, res, used,[])
        return res
    def backtracking(self, nums, res, used,temp):
        if len(temp) == len(nums):
            res.append(list(temp))
            return
        for i in range(len(nums)):
            if used[i] or i>0 and nums[i]== nums[i-1] and not used[i-1]:
                continue
            temp.append(nums[i])
            used[i] = True
            self.backtracking(nums, res, used, temp)
            used[i] = False
            temp.pop()
            
        
