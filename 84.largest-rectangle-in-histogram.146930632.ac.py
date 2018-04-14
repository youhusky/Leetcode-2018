#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (27.53%)
# Total Accepted:    114.1K
# Total Submissions: 414.4K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# 
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
# 
# 
# 
# 
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
# 
# 
# 
# 
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
# 
# 
# 
# For example,
# Given heights = [2,1,5,6,2,3],
# return 10.
# 
#
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res = 0
        stack = []
        for i in range(len(heights)+1):
            height = heights[i] if i!= len(heights) else 0
            while stack and height <= heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] -1 if stack else i
                res = max(res, h*w)
            stack.append(i)
        return res
        
