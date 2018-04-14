#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (26.74%)
# Total Accepted:    137.1K
# Total Submissions: 512.8K
# Testcase Example:  '[2,3,-2,4]'
#
# Find the contiguous subarray within an array (containing at least one number)
# which has the largest product.
# 
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.
# 
#
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        ans = nums[0]
        maxres, minres = nums[0],nums[0]
        for i in range(1,len(nums)):
            if nums[i] < 0:
                maxres, minres = minres, maxres
            maxres = max(maxres * nums[i], nums[i])
            minres = min(minres * nums[i], nums[i])
            ans = max(maxres, ans)
        return ans
