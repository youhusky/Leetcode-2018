#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (19.46%)
# Total Accepted:    98.3K
# Total Submissions: 505.3K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# 
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# 
# 
# For example,
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# 
# 
# After running your function, the board should be:
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
#
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                # border case
                if (i == 0 or j == 0 or i == m-1 or j == n -1) and board[i][j] == 'O':
                    board[i][j] == 'M'
                    self.dfs(i,j,board)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'M':
                    board[i][j] = 'O'
    
    def dfs(self, r, c, board):
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] == 'X' or board[r][c] == 'M':
            return
        board[r][c] = 'M'
        self.dfs(r+1, c, board)
        self.dfs(r-1, c, board)
        self.dfs(r, c+1, board)
        self.dfs(r, c-1, board)
