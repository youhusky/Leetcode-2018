class storage(object):
	"""docstring for storage"""
	def __init__(self):
		super(storage, self).__init__()
		self.dic = dict()
	def put(self, k,v,t):
		if k not in self.dic:
			self.dic[k] = [[t,v]]
		else:
			self.dic[k].append([t,v])

	def getall(self, k):
		if k not in self.dic:
			return 
		else:
			return self.dic[k]

	def get(self, k,t):
		if k not in self.dic:
			return
		else:
			candidate = self.dic[k]
			index = self.binarysearch(candidate, t)
			return candidate[index][1]

	def binarysearch(self,nums, target):
		l,r = 0 ,len(nums)
		while l + 1 < r:
			mid = l + (r-l)/2
			if nums[mid][0] == target:
				return mid+1
			elif nums[mid][0] < target:
				l = mid

			else:
				r = mid
		if nums[l][0] < target and nums[r][0] < target:
			return r +1
		else:
			return r

m = storage()
m.put('a',1,1)
m.put('a',1,2)
m.put('a',2,3)
m.put('a',4,5)
print m.getall('a')
print m.get('a',2)

		