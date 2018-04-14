#
# [628] Maximum Product of Three Numbers
#
# https://leetcode.com/problems/maximum-product-of-three-numbers/description/
#
# algorithms
# Easy (44.63%)
# Total Accepted:    33.4K
# Total Submissions: 74.9K
# Testcase Example:  '[1,2,3]'
#
# Given an integer array, find three numbers whose product is maximum and
# output the maximum product.
# 
# Example 1:
# 
# Input: [1,2,3]
# Output: 6
# 
# 
# 
# Example 2:
# 
# Input: [1,2,3,4]
# Output: 24
# 
# 
# 
# Note:
# 
# The length of the given array will be in range [3,104] and all elements are
# in the range [-1000, 1000].
# Multiplication of any three numbers in the input won't exceed the range of
# 32-bit signed integer.
# 
# 
#
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min1 = float('inf')
        min2 = float('inf')
        max1 = float('-inf')
        max2 = float('-inf')
        max3 = float('-inf')
        for n in nums:
            if n <= min1: 
                min2 = min1
                min1 = n
            elif n <= min2:     # n lies between min1 and min2
                min2 = n
            if n >= max1:            # n is greater than max1, max2 and max3
                max3 = max2
                max2 = max1
                max1 = n
            elif n >= max2:   # n lies betweeen max1 and max2
                max3 = max2;
                max2 = n
            elif n >= max3:    # n lies betwen max2 and max3
                max3 = n
            
        
        return max(min1 * min2 * max1, max1 * max2 * max3)
        
