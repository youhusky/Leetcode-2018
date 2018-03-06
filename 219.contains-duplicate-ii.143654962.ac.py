#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (32.80%)
# Total Accepted:    137.1K
# Total Submissions: 418.2K
# Testcase Example:  '[]\n0'
#
# 
# Given an array of integers and an integer k, find out whether there are two
# distinct indices i and j in the array such that nums[i] = nums[j] and the
# absolute difference between i and j is at most k.
# 
#
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numset = set()
        for i in range(len(nums)):
            if nums[i] in numset:
                return True
            numset.add(nums[i])
            if len(numset) > k:
                numset.remove(nums[i-k])
        return False
        
