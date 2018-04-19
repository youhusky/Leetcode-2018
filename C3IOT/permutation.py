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
            

