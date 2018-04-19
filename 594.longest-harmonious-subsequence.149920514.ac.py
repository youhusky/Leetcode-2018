#
# [594] Longest Harmonious Subsequence
#
# https://leetcode.com/problems/longest-harmonious-subsequence/description/
#
# algorithms
# Easy (41.07%)
# Total Accepted:    20.7K
# Total Submissions: 50.5K
# Testcase Example:  '[1,3,2,2,5,2,3,7]'
#
# We define a harmonious array is an array where the difference between its
# maximum value and its minimum value is exactly 1.
# 
# Now, given an integer array, you need to find the length of its longest
# harmonious subsequence among all its possible subsequences.
# 
# Example 1:
# 
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# 
# 
# 
# Note:
# The length of the input array will not exceed 20,000.
# 
# 
# 
#
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict()
        for num in nums:
            dic[num] = dic.get(num,0) + 1
        
        res = 0
        for key in dic:
            if key+1 in dic:
                res = max(res, dic[key] + dic[key+1])
        return res
