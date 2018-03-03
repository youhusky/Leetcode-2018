#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (21.80%)
# Total Accepted:    298.7K
# Total Submissions: 1.4M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array S of n integers, are there elements a, b, c in S such that a +
# b + c = 0? Find all unique triplets in the array which gives the sum of
# zero.
# 
# Note: The solution set must not contain duplicate triplets.
# 
# 
# For example, given array S = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
#
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        
        # imp
        nums = sorted(nums)
        res = []
        
        for i in range(len(nums)-2):
            # dup
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[l] + nums[r] + nums[i]
                if s == 0:
                    res.append((nums[l], nums[r], nums[i]))
                    # contain duplicate method
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                    
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return res
        
