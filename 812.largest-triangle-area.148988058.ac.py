#
# [830] Largest Triangle Area
#
# https://leetcode.com/problems/largest-triangle-area/description/
#
# algorithms
# Easy (52.21%)
# Total Accepted:    2.5K
# Total Submissions: 4.8K
# Testcase Example:  '[[0,0],[0,1],[1,0],[0,2],[2,0]]'
#
# You have a list of points in the plane. Return the area of the largest
# triangle that can be formed by any 3 of the points.
# 
# 
# Example:
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2
# Explanation: 
# The five points are show in the figure below. The red triangle is the
# largest.
# 
# 
# 
# 
# Notes: 
# 
# 
# 3 <= points.length <= 50.
# No points will be duplicated.
# -50 <= points[i][j] <= 50.
# Answers within 10^-6 of the true value will be accepted as correct.
# 
# 
# 
#
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def triangle_area(x1, y1, x2, y2, x3, y3):
            return abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
        
        res = 0
        for i in range(len(points)-2):
            for j in range(i+1,len(points)-1):
                for k in range(j+1, len(points)):
                    res = max(res, triangle_area(points[i][0],points[i][1],points[j][0],points[j][1],points[k][0],points[k][1]))
        return res
