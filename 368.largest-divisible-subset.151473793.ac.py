#
# [368] Largest Divisible Subset
#
# https://leetcode.com/problems/largest-divisible-subset/description/
#
# algorithms
# Medium (33.96%)
# Total Accepted:    34.4K
# Total Submissions: 101.3K
# Testcase Example:  '[1,2,3]'
#
# 
# Given a set of distinct positive integers, find the largest subset such that
# every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj %
# Si = 0.
# 
# 
# If there are multiple solutions, return any subset is fine.
# 
# 
# Example 1:
# 
# nums: [1,2,3]
# 
# Result: [1,2] (of course, [1,3] will also be ok)
# 
# 
# 
# Example 2:
# 
# nums: [1,2,4,8]
# 
# Result: [1,2,4,8]
# 
# 
# 
# Credits:Special thanks to @Stomach_ache for adding this problem and creating
# all test cases.
#
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        nums.sort()
        n = len(nums)
        dp, index = [1] * n, [-1] * n
        max_dp, max_index = 1, 0
        for i in xrange(n):
            for j in xrange(i-1,-1,-1):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    index[i] = j
 
            if max_dp < dp[i]:
                max_dp, max_index = dp[i], i
        #print index
        ans = []
        while max_index != -1:
            ans.append(nums[max_index])
            max_index = index[max_index]
        return ans
