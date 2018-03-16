#
# [740] Delete and Earn
#
# https://leetcode.com/problems/delete-and-earn/description/
#
# algorithms
# Medium (43.69%)
# Total Accepted:    7.3K
# Total Submissions: 16.6K
# Testcase Example:  '[3,4,2]'
#
# 
# Given an array nums of integers, you can perform operations on the array.
# 
# In each operation, you pick any nums[i] and delete it to earn nums[i]
# points.  After, you must delete every element equal to nums[i] - 1 or nums[i]
# + 1.
# 
# You start with 0 points.  Return the maximum number of points you can earn by
# applying such operations.
# 
# 
# Example 1:
# 
# Input: nums = [3, 4, 2]
# Output: 6
# Explanation: 
# Delete 4 to earn 4 points, consequently 3 is also deleted.
# Then, delete 2 to earn 2 points. 6 total points are earned.
# 
# 
# 
# Example 2:
# 
# Input: nums = [2, 2, 3, 3, 3, 4]
# Output: 9
# Explanation: 
# Delete 3 to earn 3 points, deleting both 2's and the 4.
# Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
# 9 total points are earned.
# 
# 
# 
# Note:
# The length of nums is at most 20000.
# Each element nums[i] is an integer in the range [1, 10000].
# 
#
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        N = max(nums) + 1
        numCount = [0 for i in range(N)]
        for num in nums:
            numCount[num] += 1
        
        dp = [[0, 0] for i in range(N)]
        for i in range(1, N):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + i * numCount[i]
            
        return max(dp[N-1][0], dp[N-1][1])
