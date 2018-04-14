#
# [421] Maximum XOR of Two Numbers in an Array
#
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
#
# algorithms
# Medium (47.96%)
# Total Accepted:    22.1K
# Total Submissions: 46.1K
# Testcase Example:  '[3,10,5,25,2,8]'
#
# Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai <
# 231.
# 
# Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
# 
# Could you do this in O(n) runtime?
# 
# Example:
# 
# Input: [3, 10, 5, 25, 2, 8]
# 
# Output: 28
# 
# Explanation: The maximum result is 5 ^ 25 = 28.
# 
# 
#
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mask = 0
        finalRes = 0
        for bit in xrange(31, -1, -1):
            mask |= 1 << bit
            prefixSet = {num & mask for num in nums}
            guess = finalRes | 1 << bit
            for prefix in prefixSet:
                if prefix ^ guess in prefixSet:
                    finalRes = guess
                    break
        return finalRes
