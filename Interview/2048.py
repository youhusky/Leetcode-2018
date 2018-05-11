def game(matrix,flag):
	
	i = 0
	while i < len(matrix):
		count = 0
		if flag == 1:
			j = 0
		else:
			j = len(matrix[0]) - 1
		while count < len(matrix[0])-1:
			if flag:
				if matrix[i][j] == matrix[i][j+1]:
					matrix[i][j] *= 2
					matrix[i][j+1] = 0
					count += 2
					j += 2
				else:
					count += 1
					j += 1
			else:
				if matrix[i][j] == matrix[i][j-1]:
					matrix[i][j] *= 2
					matrix[i][j-1] = 0
					count += 2
					j -= 2
				else:
					count += 1
					j -= 1
		i += 1
	print matrix
	for row in matrix:
		start = 0
		for col in row:
			if col:
				row[start] = col
				start += 1
		for i in range(start, len(matrix[0])):
			row[i] = 0

	print matrix
matrix = [[ 1, 1, 2, 2],[ 
  2, 0, 3, 3 ],[  
  0, 0, 1, 2],[
  3, 3 , 1, 2 ]]

game(matrix,1)