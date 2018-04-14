#
# [377] Combination Sum IV
#
# https://leetcode.com/problems/combination-sum-iv/description/
#
# algorithms
# Medium (42.71%)
# Total Accepted:    57.1K
# Total Submissions: 133.7K
# Testcase Example:  '[1,2,3]\n4'
#
# ⁠Given an integer array with all positive numbers and no duplicates, find the
# number of possible combinations that add up to a positive integer target.
# 
# Example:
# 
# nums = [1, 2, 3]
# target = 4
# 
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# 
# Note that different sequences are counted as different combinations.
# 
# Therefore the output is 7.
# 
# 
# 
# Follow up:
# What if negative numbers are allowed in the given array?
# How does it change the problem?
# What limitation we need to add to the question to allow negative numbers? 
# 
# Credits:Special thanks to @pbrother for adding this problem and creating all
# test cases.
#
class Solution(object):
    def combinationSum4(self, nums, target):
        # dp similar to coin change
        nums, dp = sorted(nums), [1] + [0] * (target)
        for i in range(target + 1):
            for num in nums:
                if num  > i: break
                if num == i: dp[i] += 1
                if num  < i: dp[i] += dp[i - num]
        return dp[target]
