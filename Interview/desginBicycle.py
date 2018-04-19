class Solution(object):
	"""docstring for Solution"""
	def __init__(self):
		super(Solution, self).__init__()
		self.matrix = [[0,1,0,1],
						[0,0,0,0],
						[-1,0,-1,0]]

		self.person = [[2,0],[2,2]]
		self.bicycle = [[0,1],[0,3]]
		self.visited = set()
		self.res = []
		

	def find(self, i,j):
		point = [i,j]
		queue = [[i,j,0]]
		direction = [(1,0),(0,1),(-1,0),(0,-1)]
		dic = dict()
		while queue:
			r,c,count = queue.pop(0)
			dic[(r,c)] = count
			for x,y in direction:
				row = r+x
				col = c +y
				#if 0 <= row < len(self.matrix) and 0 <= col < len(self.matrix[0]):
				if [row, col] in self.bicycle:
					self.res.append(count+1)
					self.visited.add((row, col))
					return self.res
				if [row, col] not in self.bicycle and [row, col] not in self.person:
					prev = dic.get((row, col),0)
					dic[(row, col)] = count+1
					if dic[(row,col)] > 0 and prev <= count+1 and prev:
						continue

					queue.append((row, col,count+1))
		return [-1]

	def main(self):
		if len(self.person) != len(self.bicycle):
			return False
		for each in self.person:
			if self.find(each[0],each[1]) == [-1]:
				return False
			print self.res
		return True
	def printmatrix(self):
		print self.res,self.visited

m = Solution()
print m.main()







		