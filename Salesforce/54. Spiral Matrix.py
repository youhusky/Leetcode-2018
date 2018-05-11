class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix or not matrix[0]:
            return res
        m = len(matrix)
        n = len(matrix[0])
        
        
        while matrix:
            # 1,2,3
            res += matrix.pop(0)
            # down
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix:
                res += matrix.pop()[::-1]
            
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res

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
                