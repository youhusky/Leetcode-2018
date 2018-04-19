def uniquePaths(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    if not m or not n:
        return 0
    dp = [[1 for _ in range(n)] for _ in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]

def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [[0] *n] * m
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            elif i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]

def helper(matrix,m,n,temp,res,pos):
    if m == len(matrix)-1 and n == len(matrix[0])-1:
        temp[pos] = matrix[m][n]
        res.append(list(temp))
        return
    if m >= len(matrix)  or n >= len(matrix[0]):
        return
    temp[pos] = matrix[m][n]
    helper(matrix,m,n+1, temp,res,pos+1)
    helper(matrix, m+1, n, temp,res,pos+1)
    

def PrintAllPathFromTopLeftToBottomRight(matrix):
    res = []
    temp = [0 for _ in range(len(matrix)+len(matrix[0])-1)]
    helper(matrix, 0,0,temp,res,0)
    return res

matrix = [[1,2,3],[4,5,6]]
print(PrintAllPathFromTopLeftToBottomRight(matrix))