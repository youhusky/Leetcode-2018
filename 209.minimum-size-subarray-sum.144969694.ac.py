#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (32.01%)
# Total Accepted:    111.6K
# Total Submissions: 348.4K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 
# Given an array of n positive integers and a positive integer s, find the
# minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
# one, return 0 instead.
# 
# 
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.
# 
# 
# click to show more practice.
# 
# More practice:
# 
# If you have figured out the O(n) solution, try coding another solution of
# which the time complexity is O(n log n).
# 
# 
# Credits:Special thanks to @Freezen for adding this problem and creating all
# test cases.
#
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # sliding widows
        if not nums:
            return 0
        l, r = 0, 0
        minLength = len(nums)+1
        res = 0
        while r < len(nums):
            res += nums[r]
            
            r += 1
            
            while res >= s:
                minLength = min(minLength, r - l)
                res -= nums[l]
                l += 1
        return 0 if minLength == len(nums)+1 else minLength
        
