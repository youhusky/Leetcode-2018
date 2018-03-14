#
# [36] Valid Sudoku
#
# https://leetcode.com/problems/valid-sudoku/description/
#
# algorithms
# Medium (37.40%)
# Total Accepted:    148.3K
# Total Submissions: 396.6K
# Testcase Example:  '[[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]'
#
# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
# 
# The Sudoku board could be partially filled, where empty cells are filled with
# the character '.'.
# 
# 
# 
# A partially filled sudoku which is valid.
# 
# 
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the
# filled cells need to be validated.
# 
#
class Solution(object):
    def test_rows(self, board):
        for i in range(9):
            dedup = set([])
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in dedup:
                        return False
                    elif int(board[i][j]) < 0 or int(board[i][j]) > 9:
                        return False 
                    else:
                        dedup.add(board[i][j])
        return True
    
    def test_cols(self, board):
        for j in range(9):
            dedup = set([])
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] in dedup:
                        return False
                    elif int(board[i][j]) < 0 or int(board[i][j]) > 9:
                        return False 
                    else:
                        dedup.add(board[i][j])
        return True    
    
    def test_grid(self, rs, cs, board):
        dedup = set([])
        for i in range(rs, rs+3):
            for j in range(cs, cs+3):
                if board[i][j] != ".":
                    if board[i][j] in dedup:
                        return False
                    elif int(board[i][j]) < 0 or int(board[i][j]) > 9:
                        return False 
                    else:
                        dedup.add(board[i][j])
        return True
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if self.test_rows(board) == False:
            return False
        if self.test_cols(board) == False:
            return False
        for rs in range(0,9,3):
            for cs in range(0, 9, 3):
                if self.test_grid(rs, cs, board) == False:
                    return False
        return True
