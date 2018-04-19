#
# [442] Find All Duplicates in an Array
#
# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
#
# algorithms
# Medium (56.99%)
# Total Accepted:    56.3K
# Total Submissions: 98.7K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements
# appear twice and others appear once.
# 
# Find all the elements that appear twice in this array.
# 
# Could you do it without extra space and in O(n) runtime?
# 
# Example:
# 
# Input:
# [4,3,2,7,8,2,3,1]
# 
# Output:
# [2,3]
# 
#
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # similiar to Find All Numbers Disappeared in an Array
        res = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
        return res
