#
# [532] K-diff Pairs in an Array
#
# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/
#
# algorithms
# Easy (28.19%)
# Total Accepted:    33.7K
# Total Submissions: 119.5K
# Testcase Example:  '[3,1,4,1,5]\n2'
#
# 
# Given an array of integers and an integer k, you need to find the number of
# unique k-diff pairs in the array. Here a k-diff pair is defined as an integer
# pair (i, j), where i and j are both numbers in the array and their absolute
# difference is k.
# 
# 
# 
# Example 1:
# 
# Input: [3, 1, 4, 1, 5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3,
# 5).Although we have two 1s in the input, we should only return the number of
# unique pairs.
# 
# 
# 
# Example 2:
# 
# Input:[1, 2, 3, 4, 5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4)
# and (4, 5).
# 
# 
# 
# Example 3:
# 
# Input: [1, 3, 1, 5, 4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).
# 
# 
# 
# Note:
# 
# The pairs (i, j) and (j, i) count as the same pair.
# The length of the array won't exceed 10,000.
# All the integers in the given input belong to the range: [-1e7, 1e7].
# 
# 
#
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {}
        res = 0
        for num in nums:
            if num not in dic: 
                dic[num] = 1 
            else:
                dic[num] += 1
        # divide into two parts one is num + k in array and the other is when k ==0 count its appearence
        for num in dic:
            if k > 0 and num + k in dic or k == 0 and dic[num] > 1:
                res += 1
        return res
        
