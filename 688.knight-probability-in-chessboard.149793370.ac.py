#
# [688] Knight Probability in Chessboard
#
# https://leetcode.com/problems/knight-probability-in-chessboard/description/
#
# algorithms
# Medium (40.00%)
# Total Accepted:    6.8K
# Total Submissions: 17K
# Testcase Example:  '3\n2\n0\n0'
#
# 
# On an NxN chessboard, a knight starts at the r-th row and c-th column and
# attempts to make exactly K moves.  The rows and columns are 0 indexed, so the
# top-left square is (0, 0), and the bottom-right square is (N-1, N-1).
# 
# 
# 
# A chess knight has 8 possible moves it can make, as illustrated below.  Each
# move is two squares in a cardinal direction, then one square in an orthogonal
# direction.
# 
# 
# 
# 
# 
# Each time the knight is to move, it chooses one of eight possible moves
# uniformly at random (even if the piece would go off the chessboard) and moves
# there.
# 
# 
# 
# The knight continues moving until it has made exactly K moves or has moved
# off the chessboard.  Return the probability that the knight remains on the
# board after it has stopped moving.
# 
# 
# Example:
# 
# Input: 3, 2, 0, 0
# Output: 0.0625
# Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight
# on the board.
# From each of those positions, there are also two moves that will keep the
# knight on the board.
# The total probability the knight stays on the board is 0.0625.
# 
# 
# 
# Note:
# N will be between 1 and 25.
# K will be between 0 and 100.
# The knight always initially starts on the board.
# 
#
class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        self.memo = {}
        self.N = N
        return self.dfs(K,r,c)
    
    def dfs(self,k,r,c):
        if (k,r,c) in self.memo:
            return self.memo[(k,r,c)]
        # no more step
        if k == 0:
            return 1
        res = 0
        for x, y in ((2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)):
            if 0 <= r+x < self.N and 0 <= c+y < self.N:
                res += self.dfs(k-1,r+x, c+y) * 0.125
        self.memo[(k,r,c)] = res
        return res
        
        
