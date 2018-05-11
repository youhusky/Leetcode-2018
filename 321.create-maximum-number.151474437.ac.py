#
# [321] Create Maximum Number
#
# https://leetcode.com/problems/create-maximum-number/description/
#
# algorithms
# Hard (24.86%)
# Total Accepted:    23.6K
# Total Submissions: 94.9K
# Testcase Example:  '[3,4,6,5]\n[9,1,2,5,8,3]\n5'
#
# 
# ⁠   Given two arrays of length m and n with digits 0-9 representing two
# numbers.
# ⁠   Create the maximum number of length k  from digits of the two. The
# relative order of the digits
# ⁠   from the same array must be preserved. Return an array of the k digits.
# You should try to optimize your time and space complexity.
# 
# 
# 
# ⁠   Example 1:
# 
# 
# ⁠   nums1 = [3, 4, 6, 5]
# ⁠   nums2 = [9, 1, 2, 5, 8, 3]
# ⁠   k = 5
# ⁠   return [9, 8, 6, 5, 3]
# 
# 
# ⁠   Example 2:
# 
# 
# ⁠   nums1 = [6, 7]
# ⁠   nums2 = [6, 0, 4]
# ⁠   k = 5
# ⁠   return [6, 7, 6, 0, 4]
# 
# 
# ⁠   Example 3:
# 
# 
# ⁠   nums1 = [3, 9]
# ⁠   nums2 = [8, 9]
# ⁠   k = 3
# ⁠   return [9, 8, 9]
# 
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
 
        def get_max_sub_array(nums, k):
            res , n = [] ,len(nums)
            for i in xrange(n):
                while res and len(res) + n - i > k and nums[i] > res[-1]:
                    res.pop()
                if len(res) < k:
                    res.append(nums[i])
            return res
 
        ans = [0] * k
        for i in xrange(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            res1 = get_max_sub_array(nums1, i)
            res2 = get_max_sub_array(nums2, k - i)
            ans = max(ans, [max(res1, res2).pop(0) for _ in xrange(k)])
        return ans
