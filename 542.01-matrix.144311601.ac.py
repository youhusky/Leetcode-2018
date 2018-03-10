#
# [542] 01 Matrix
#
# https://leetcode.com/problems/01-matrix/description/
#
# algorithms
# Medium (32.91%)
# Total Accepted:    18.4K
# Total Submissions: 55.9K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for
# each cell.
# 
# The distance between two adjacent cells is 1.
# 
# Example 1: 
# Input:
# 
# 0 0 0
# 0 1 0
# 0 0 0
# 
# Output:
# 
# 0 0 0
# 0 1 0
# 0 0 0
# 
# 
# 
# Example 2: 
# Input:
# 
# 0 0 0
# 0 1 0
# 1 1 1
# 
# Output:
# 
# 0 0 0
# 0 1 0
# 1 2 1
# 
# 
# 
# Note:
# 
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.
# 
# 
# 
#
class Solution(object):
    def updateMatrix(self, rooms):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
    
        queue = []
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == 0:
                    queue.append((row,col))
                else:
                    rooms[row][col] = float('inf')
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        while queue:
            i,j = queue.pop(0)
            for x,y in direction:
                row = i + x
                col = j + y
                if 0 <= row < len(rooms) and 0 <= col < len(rooms[0]) and rooms[row][col] > 1 + rooms[i][j]:
                    rooms[row][col] = rooms[i][j] + 1
                    queue.append((row, col))

        return rooms
