#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (47.79%)
# Total Accepted:    245.9K
# Total Submissions: 514.6K
# Testcase Example:  '[1]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        res = 0
        for num in nums:
            if count == 0:
                res = num
            if res != num:
                count -= 1
            else:
                count += 1
        return res
        
