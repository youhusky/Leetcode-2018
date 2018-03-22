#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (37.50%)
# Total Accepted:    158.3K
# Total Submissions: 422.2K
# Testcase Example:  '[]'
#
# 
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after
# raining. 
# 
# 
# 
# For example, 
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
# 
# 
# 
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
#
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        i = 0
        stack = []
        
        while i < len(height):
       
            while stack and height[i] > height[stack[-1]]:
    
                top = stack.pop()
                
                
                
                # find the left bound
                if not stack:
                    break
                    
                distance = i - stack[-1] - 1
                bound_height = min(height[i], height[stack[-1]]) - height[top]
                res += distance * bound_height
                
            stack.append(i)
            i += 1
            
        return res
