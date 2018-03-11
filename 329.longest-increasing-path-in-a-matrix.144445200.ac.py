#
# [329] Longest Increasing Path in a Matrix
#
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (37.33%)
# Total Accepted:    49.6K
# Total Submissions: 133K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# Given an integer matrix, find the length of the longest increasing path.
# 
# 
# From each cell, you can either move to four directions: left, right, up or
# down. You may NOT move diagonally or move outside of the boundary (i.e.
# wrap-around is not allowed).
# 
# 
# Example 1:
# 
# nums = [
# ⁠ [9,9,4],
# ⁠ [6,6,8],
# ⁠ [2,1,1]
# ]
# 
# 
# 
# 
# Return 4
# 
# The longest increasing path is [1, 2, 6, 9].
# 
# 
# Example 2:
# 
# nums = [
# ⁠ [3,4,5],
# ⁠ [3,2,6],
# ⁠ [2,2,1]
# ]
# 
# 
# 
# 
# Return 4
# 
# The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not
# allowed.
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        
        cache = [[0 for _ in range(n)] for _ in range(m)]
        
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, self.dfs(i,j,cache, matrix))
        return ans
    
    def dfs(self, i, j, cache, matrix):
        # find cache
        if cache[i][j] != 0:
            return cache[i][j]
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        for dire in direction:
            x, y = i + dire[0], j + dire[1]
            if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]) or matrix[i][j] >= matrix[x][y]:
                continue
            cache[i][j] = max(cache[i][j], self.dfs(x,y,cache, matrix))
        # self (i,j) + 1
        cache[i][j] += 1
        return cache[i][j]
        
