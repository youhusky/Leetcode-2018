def searchMatrix(matrix,target):
	if not matrix or not matrix[0]:
		return False
	m,n = len(matrix), len(matrix[0])
	row, col = 0, n-1
	while row < m and col >= 0:
		if target == matrix[row][col]:
			return True
		elif target < matrix[row][col]:
			col -= 1
		else:
			row += 1
	return False
