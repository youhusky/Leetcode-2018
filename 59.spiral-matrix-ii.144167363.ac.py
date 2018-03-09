#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (40.82%)
# Total Accepted:    97.5K
# Total Submissions: 238.8K
# Testcase Example:  '0'
#
# Given an integer n, generate a square matrix filled with elements from 1 to
# n2 in spiral order.
# 
# 
# For example,
# Given n = 3,
# 
# You should return the following matrix:
# 
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
# 
#
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        left, right, up, down = 0, n-1, 0, n-1
        num = 1
        
        while left <= right and up <= down:
            for i in range(left, right+1):
                matrix[up][i] = num
                num += 1
            # up already occupied
            for j in range(up+1, down):
                matrix[j][right] = num
                num += 1
            # bottom
            for i in range(right, left-1, -1):
                if up < down:
                    matrix[down][i] = num
                    num += 1
                
            # left
            for j in range(down-1, up, -1):
                if left < right:
                    matrix[j][left] = num
                    num += 1
            left, right, up, down = left+1, right -1, up+1, down-1
            
        return matrix
                
