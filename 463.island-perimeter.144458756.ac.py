#
# [463] Island Perimeter
#
# https://leetcode.com/problems/island-perimeter/description/
#
# algorithms
# Easy (57.82%)
# Total Accepted:    73.7K
# Total Submissions: 127.5K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# You are given a map in form of a two-dimensional integer grid where 1
# represents land and 0 represents water. Grid cells are connected
# horizontally/vertically (not diagonally). The grid is completely surrounded
# by water, and there is exactly one island (i.e., one or more connected land
# cells). The island doesn't have "lakes" (water inside that isn't connected to
# the water around the island). One cell is a square with side length 1. The
# grid is rectangular, width and height don't exceed 100. Determine the
# perimeter of the island.
# 
# Example:
# 
# [[0,1,0,0],
# ⁠[1,1,1,0],
# ⁠[0,1,0,0],
# ⁠[1,1,0,0]]
# 
# Answer: 16
# Explanation: The perimeter is the 16 yellow stripes in the image below:
# 
# 
# 
#
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 1):
                    for m,n in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                        if (m<0 or m>=rows or n<0 or n>=cols or grid[m][n] == 0):
                            count += 1
        return count
