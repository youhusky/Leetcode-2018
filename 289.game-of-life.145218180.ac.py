#
# [289] Game of Life
#
# https://leetcode.com/problems/game-of-life/description/
#
# algorithms
# Medium (37.26%)
# Total Accepted:    64.6K
# Total Submissions: 173.3K
# Testcase Example:  '[[]]'
#
# 
# According to the Wikipedia's article: "The Game of Life, also known simply as
# Life, is a cellular automaton devised by the British mathematician John
# Horton Conway in 1970."
# 
# 
# 
# Given a board with m by n cells, each cell has an initial state live (1) or
# dead (0). Each cell interacts with its eight neighbors (horizontal, vertical,
# diagonal) using the following four rules (taken from the above Wikipedia
# article):
# 
# 
# 
# 
# Any live cell with fewer than two live neighbors dies, as if caused by
# under-population.
# Any live cell with two or three live neighbors lives on to the next
# generation.
# Any live cell with more than three live neighbors dies, as if by
# over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by
# reproduction.
# 
# 
# 
# 
# Write a function to compute the next state (after one update) of the board
# given its current state.
# 
# 
# Follow up: 
# 
# Could you solve it in-place? Remember that the board needs to be updated at
# the same time: You cannot update some cells first and then use their updated
# values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the
# board is infinite, which would cause problems when the active area encroaches
# the border of the array. How would you address these problems?
# 
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        O(n^2), O(1)
        """
        def getValue(board, i, j):
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
                return 0
            else:
                #print board[i][j]
                return board[i][j] & 1
        dx = (1, 1, 1, 0, 0, -1, -1, -1)
        dy = (1, 0, -1, 1, -1, 1, 0, -1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                live = 0
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    live += getValue(board, nx, ny)
                if live + board[i][j] == 3 or live == 3:
                    # store status because value only be 1/0
                    board[i][j] |= 2 # 10
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] >>= 1 # right move
