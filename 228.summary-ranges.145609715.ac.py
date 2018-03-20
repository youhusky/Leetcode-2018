#
# [228] Summary Ranges
#
# https://leetcode.com/problems/summary-ranges/description/
#
# algorithms
# Medium (31.89%)
# Total Accepted:    96.2K
# Total Submissions: 301.7K
# Testcase Example:  '[0,1,2,4,5,7]'
#
# 
# Given a sorted integer array without duplicates, return the summary of its
# ranges.
# 
# Example 1:
# 
# Input: [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# 
# 
# 
# Example 2:
# 
# Input: [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# 
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        res = []
        start = 0
        i = 0
        
        # not contains the last
        while i < len(nums) - 1:
            if nums[i] + 1 != nums[i+1]:
                res.append(self.helper(nums[start], nums[i]))
                start = i + 1
            i += 1
        res.append(self.helper(nums[start], nums[i]))
        return res
        
    def helper(self, l, r):
        
        return str(l) if l == r else str(l) + "->" + str(r)
