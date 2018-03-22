#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (31.62%)
# Total Accepted:    168.6K
# Total Submissions: 533.1K
# Testcase Example:  '[0,0,0]\n1'
#
# Given an array S of n integers, find three integers in S such that the sum is
# closest to a given number, target. Return the sum of the three integers. You
# may assume that each input would have exactly one solution.
# 
# 
# ⁠   For example, given array S = {-1 2 1 -4}, and target = 1.
# 
# ⁠   The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
#
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num = sorted(num)
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            while j < k:
                temp = num[i] + num[j] + num[k]
                if temp == target:
                    return temp
                
                if abs(temp - target) < abs(result - target):
                    result = temp
                
                if temp < target:
                    j += 1
                elif temp > target:
                    k -= 1
            
        return result
