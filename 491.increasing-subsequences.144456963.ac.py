#
# [491] Increasing Subsequences
#
# https://leetcode.com/problems/increasing-subsequences/description/
#
# algorithms
# Medium (38.76%)
# Total Accepted:    16.8K
# Total Submissions: 43.4K
# Testcase Example:  '[4,6,7,7]'
#
# 
# Given an integer array, your task is to find all the different possible
# increasing subsequences of the given array, and the length of an increasing
# subsequence should be at least 2 .
# 
# 
# Example:
# 
# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7],
# [4,7,7]]
# 
# 
# 
# Note:
# 
# The length of the given array will not exceed 15.
# The range of integer in the given array is [-100,100].
# The given array may contain duplicates, and two equal integers should also be
# considered as a special case of increasing sequence.
# 
# 
#
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.subsets(nums, 0, [], res)
        return res
        
    def subsets(self, nums, index, temp, res):
        if len(nums) >= index and len(temp) >= 2:
            res.append(list(temp))
        used = {}
        for i in range(index, len(nums)):
            if len(temp) > 0 and temp[-1] > nums[i]: 
                continue
            if nums[i] in used: 
                continue
            used[nums[i]] = True
            temp.append(nums[i])
            self.subsets(nums, i+1, temp, res)
            temp.pop()
