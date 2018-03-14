#
# [37] Sudoku Solver
#
# https://leetcode.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (31.93%)
# Total Accepted:    89.5K
# Total Submissions: 280.3K
# Testcase Example:  '[[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]'
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# 
# Empty cells are indicated by the character '.'.
# 
# You may assume that there will be only one unique solution.
# 
# 
# 
# A sudoku puzzle...
# 
# 
# 
# 
# ...and its solution numbers marked in red.
# 
#
class Solution(object):
    def solveSudoku(self, board):
        def isValid(board, x, y):
            for i in xrange(9):
                if i != x and board[i][y] == board[x][y]:
                    return False
            for j in xrange(9):
                if j != y and board[x][j] == board[x][y]:
                    return False
            i = 3 * (x / 3)
            while i < 3 * (x / 3 + 1):
                j = 3 * (y / 3)
                while j < 3 * (y / 3 + 1):
                    if (i != x or j != y) and board[i][j] == board[x][y]:
                        return False
                    j += 1
                i += 1
            return True
        
        def solver(board):
            for i in xrange(len(board)):
                for j in xrange(len(board[0])):
                    if(board[i][j] == '.'):
                        for k in xrange(9):
                            board[i][j] = chr(ord('1') + k)
                            if isValid(board, i, j) and solver(board):
                                return True
                            board[i][j] = '.'
                        return False
            return True

        solver(board)
        
