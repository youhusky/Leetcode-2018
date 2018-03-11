#
# [695] Max Area of Island
#
# https://leetcode.com/problems/max-area-of-island/description/
#
# algorithms
# Easy (51.70%)
# Total Accepted:    21.8K
# Total Submissions: 42.1K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.)  You
# may assume all four edges of the grid are surrounded by water.
# 
# Find the maximum area of an island in the given 2D array.
# (If there is no island, the maximum area is 0.)
# 
# Example 1:
# 
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,1,1,0,1,0,0,0,0,0,0,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,0,1,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,1,1,0,0],
# ⁠[0,0,0,0,0,0,0,0,0,0,1,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 
# Given the above grid, return 6.
# 
# Note the answer is not 11, because the island must be connected
# 4-directionally.
# 
# 
# Example 2:
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# 
# 
# Note:
# The length of each dimension in the given grid does not exceed 50.
# 
#
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        seen = set()  # function scope var 
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    res = max(res,self.dfs(row, col, grid,seen))
        return res

    def dfs(self, row, col,grid, seen):
            """if a point is valid, it should meet all requirements using "and" """
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and (grid[row][col] == 1) and (row, col) not in seen:
                seen.add((row, col))             # list this point to seen set so we won't count it again
                return (self.dfs(row - 1, col,grid,seen) + self.dfs(row + 1, col,grid,seen)
                        + self.dfs(row, col - 1,grid,seen) + self.dfs(row, col + 1,grid, seen)
                        + 1)                     # add 1 to the area and DFS(4-Conn Neighbors)

            else:
                return 0                         # not valid point return 0


        
