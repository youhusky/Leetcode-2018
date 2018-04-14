#
# [494] Target Sum
#
# https://leetcode.com/problems/target-sum/description/
#
# algorithms
# Medium (43.79%)
# Total Accepted:    49.9K
# Total Submissions: 113.9K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# 
# You are given a list of non-negative integers, a1, a2, ..., an, and a target,
# S. Now you have 2 symbols + and -. For each integer, you should choose one
# from + and - as its new symbol.
# ⁠
# 
# Find out how many ways to assign symbols to make sum of integers equal to
# target S.  
# 
# 
# Example 1:
# 
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 
# 
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 
# There are 5 ways to assign symbols to make the sum of nums be target 3.
# 
# 
# 
# Note:
# 
# The length of the given array is positive and will not exceed 20. 
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.
# 
# 
#
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """        
        self.cache = {}
        self.nums = nums
        return self.findTarget(0, S)
    
    def findTarget(self,i, target):
        if (i, target) not in self.cache:
            res = 0
            if i == len(self.nums):
                if target == 0:
                    res = 1
            else:
                res = self.findTarget(i+1, target-self.nums[i]) + self.findTarget(i+1, target+self.nums[i])
            self.cache[(i, target)] = res
        return self.cache[(i, target)]
    
    # def findTargetSumWays(self, nums, S):
    # count = {0: 1}
    # for x in nums:
    #   count2 = {}
    #   for tmpSum in count:
    #     count2[tmpSum + x] = count2.get(tmpSum + x, 0) + count[tmpSum]
    #     count2[tmpSum - x] = count2.get(tmpSum - x, 0) + count[tmpSum]
    #   count = count2
    # return count.get(S, 0)
