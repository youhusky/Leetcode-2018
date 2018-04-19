#
# [661] Image Smoother
#
# https://leetcode.com/problems/image-smoother/description/
#
# algorithms
# Easy (46.09%)
# Total Accepted:    17.1K
# Total Submissions: 37.2K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a 2D integer matrix M representing the gray scale of an image, you need
# to design a smoother to make the gray scale of each cell becomes the average
# gray scale (rounding down) of all the 8 surrounding cells and itself.  If a
# cell has less than 8 surrounding cells, then use as many as you can.
# 
# Example 1:
# 
# Input:
# [[1,1,1],
# ⁠[1,0,1],
# ⁠[1,1,1]]
# Output:
# [[0, 0, 0],
# ⁠[0, 0, 0],
# ⁠[0, 0, 0]]
# Explanation:
# For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
# 
# 
# 
# Note:
# 
# The value in the given matrix is in the range of [0, 255].
# The length and width of the given matrix are in the range of [1, 150].
# 
# 
#
class Solution(object):
    def imageSmoother(self, M):
        if not M: return M
        helper = [[0 for _ in range(len(M[0]))] for _ in range(len(M))]
        directions = ((0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1))
        for i in range(len(helper)):
            for j in range(len(helper[0])):
                total = 0
                count = 0
                for r, c in directions:
                    if 0 <= i+r < len(helper) and 0 <= j+c < len(helper[0]): 
                        total += M[i + r][j + c]
                        count += 1
                helper[i][j] = total/count
        return helper
