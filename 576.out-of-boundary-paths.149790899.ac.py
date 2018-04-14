#
# [576] Out of Boundary Paths
#
# https://leetcode.com/problems/out-of-boundary-paths/description/
#
# algorithms
# Medium (30.62%)
# Total Accepted:    9.6K
# Total Submissions: 31.4K
# Testcase Example:  '2\n2\n2\n0\n0'
#
# There is an m by n grid with a ball. Given the start coordinate (i,j) of the
# ball, you can move the ball to adjacent cell or cross the grid boundary in
# four directions (up, down, left, right). However, you can at most move N
# times. Find out the number of paths to move the ball out of grid boundary.
# The answer may be very large, return it after mod 109 + 7.
# 
# Example 1:
# 
# Input:m = 2, n = 2, N = 2, i = 0, j = 0
# Output: 6
# Explanation:
# 
# 
# 
# 
# Example 2:
# 
# Input:m = 1, n = 3, N = 3, i = 0, j = 1
# Output: 12
# Explanation:
# 
# 
# 
# 
# Note:
# 
# Once you move the ball out of boundary, you cannot move it back.
# The length and height of the grid is in range [1,50].
# N is in range [0,50].
# 
# 
#
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        # O(mnN)
        self.memo = {}
        return self.dfs(m,n,N,i,j)% (10**9 + 7)
    
    def dfs(self,m,n,N,i,j):
        if (N,i,j) in self.memo:
            return self.memo[(N,i,j)]
        # no more step
        if N == 0:
            return 0
        res = 0
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if 0 <= i+x < m and 0 <= j+y < n:
                res += self.dfs(m,n,N-1, i+x, j+y)
            else:
                res += 1
        self.memo[(N,i,j)] = res
        return res
        
