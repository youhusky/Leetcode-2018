#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (38.11%)
# Total Accepted:    134.8K
# Total Submissions: 353.7K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# 
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
# 
# 
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length:
# 4.
# 
# 
# Your algorithm should run in O(n) complexity.
# 
#
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # interesting question
        if not nums:
            return 0
        setNum = set(nums)
        res = 0
        for num in nums:
            # mininum number
            if num-1 not in setNum:
                temp = num
                curr = 1
                while temp+1 in setNum:
                    temp += 1
                    curr += 1
                res = max(res, curr)
        return res
                
            
