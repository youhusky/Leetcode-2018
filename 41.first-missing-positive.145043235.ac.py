#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (25.83%)
# Total Accepted:    127.1K
# Total Submissions: 492.2K
# Testcase Example:  '[1,2,0]'
#
# 
# Given an unsorted integer array, find the first missing positive integer.
# 
# 
# 
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
# 
# 
# 
# Your algorithm should run in O(n) time and uses constant space.
# 
#
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict()
        for n in nums:
            if n > 0:
                dic[n] = True
        v = 1
        while True:
            if v not in dic:
                break
            v += 1
        return v
        
