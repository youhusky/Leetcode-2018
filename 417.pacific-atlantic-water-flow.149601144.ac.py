#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (34.52%)
# Total Accepted:    23.5K
# Total Submissions: 68.1K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# Given an m x n matrix of non-negative integers representing the height of
# each unit cell in a continent, the "Pacific ocean" touches the left and top
# edges of the matrix and the "Atlantic ocean" touches the right and bottom
# edges.
# 
# Water can only flow in four directions (up, down, left, or right) from a cell
# to another one with height equal or lower.
# 
# Find the list of grid coordinates where water can flow to both the Pacific
# and Atlantic ocean.
# 
# Note:
# 
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# 
# 
# Example:
# 
# Given the following 5x5 matrix:
# 
# ⁠ Pacific ~   ~   ~   ~   ~ 
# ⁠      ~  1   2   2   3  (5) *
# ⁠      ~  3   2   3  (4) (4) *
# ⁠      ~  2   4  (5)  3   1  *
# ⁠      ~ (6) (7)  1   4   5  *
# ⁠      ~ (5)  1   1   2   4  *
# ⁠         *   *   *   *   * Atlantic
# 
# Return:
# 
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with
# parentheses in above matrix).
# 
# 
#
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # O(MN) 
        # need to write more
        if not matrix or not matrix[0]:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        
        p_visited = [[False for _ in range(n)] for _ in range(m)]
        a_visited = [[False for _ in range(n)] for _ in range(m)]
        
        res = []
        for i in range(m):
            # left and right
            
            self.dfs(i, 0, p_visited, m, n, matrix)
            self.dfs(i, n-1, a_visited, m, n, matrix)
            
        for j in range(n):
            # up and down
            self.dfs(0, j, p_visited, m, n, matrix)
            self.dfs(m-1, j, a_visited, m, n, matrix)
        #print p_visited, a_visited
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    res.append([i,j])
        return res
    
    def dfs(self, i, j, visited, m, n, matrix):
        visited[i][j] = True
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        for dire in direction:
            x, y = i + dire[0], j + dire[1]
            if x < 0 or y < 0 or x >= m or y >= n or visited[x][y] or matrix[i][j] > matrix[x][y]:
                continue
            self.dfs(x, y, visited, m, n, matrix)
        
            
        
