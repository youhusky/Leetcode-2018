#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (29.00%)
# Total Accepted:    142.2K
# Total Submissions: 490.3K
# Testcase Example:  '[1,2,3]'
#
# 
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
# 
# 
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
# 
# 
# The replacement must be in-place, do not allocate extra memory.
# 
# 
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        j = -1
        
        while i > 0:
            if nums[i-1] < nums[i]:
                # find
                j = i-1
                break
            i -= 1
            
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[j]:
                # find first one larger than prev
                nums[i], nums[j] = nums[j], nums[i]
                nums[j+1: ] = sorted(nums[j+1:])
                return
