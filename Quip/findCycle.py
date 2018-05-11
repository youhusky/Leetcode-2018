from collections import defaultdict
def checkCycle(matrix):
	indegree = defaultdict(int)
	outdegree = defaultdict(list)

	queue = []
	# find zero indegree
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			node = matrix[i][j]
			origin = chr(ord('A') + j) + str(i)
			outdegree[origin].append(node)
			indegree[node] += 1
	for key in outdegree:
		if key not in indegree:
			queue.append(key)
	print queue,indegree
	res = []
	while queue:
		node = queue.pop(0)
		res.append(node)
		for pointer in outdegree[node]:
			indegree[pointer] -= 1
			if indegree[pointer] == 0:
				queue.append(pointer)
		print indegree,res



matrix = [['C1','A1','B2'],['C2','B0','B2'],['B1','A0','B1']]
checkCycle(matrix)