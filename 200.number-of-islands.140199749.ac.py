#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (36.20%)
# Total Accepted:    156K
# Total Submissions: 430.9K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 11110110101100000000
# Answer: 1
# Example 2:
# 11000110000010000011
# Answer: 3
# 
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
#
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # corner
        if not grid or not grid[0]:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        
        group = [0 for i in range(m*n)]
        
        # check
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    group[i*n+j] = i*n+j
                else:
                    group[i*n+j] = -1
                    
        count = 0
        
        # check union
        for i in range(m):
            for j in range(n):
                
                # pass one condition
                if grid[i][j] == '0':
                    continue
                if i + 1 < m and grid[i+1][j] == '1':
                    self.union(i,j,i+1,j,group,n)
                if j+1 < n and grid[i][j+1] == '1':
                    self.union(i,j,i,j+1, group,n)
        # conut
        count = 0
        for i in range(m*n):
            if group[i] == i:
                count += 1
                
        return count
        
    def find(self, e, group):
        if e == group[e]:
            return e
        else:
            return self.find(group[e], group)
        
    def union(self, i,j,k,l, group, n):
        index1 = i*n+j
        index2 = k*n+l
        root1 = self.find(index1, group)
        root2 = self.find(index2, group)
        # already union
        if root1 == root2:
            return
        else:
            group[root2] = root1
        
