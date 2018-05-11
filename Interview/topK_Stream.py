from heapq import *
class Solution(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.pq = []
		self.visit = set()

	def addWord(self, word):
		if word not in self.visit:
			self.visit.add(word)
			heappush(self.pq, [-1, word])
		else:
			for w in self.pq:
				if w[1] == word:
					changed = w
			temp = changed
			self.pq.remove(changed)
			temp[0] -= 1
			heappush(self.pq, temp)

	def getTopK(self,k):
		res = []
		while k:
			res.append(heappop(self.pq)[1])
			k -= 1
		return res

from heapq import *
class Solution2(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.pq = []
		self.dic = dict()
		self.k = 1

	def addWord(self, word):
		self.dic[word] = self.dic.get(word,0) + 1
		flag = False
		for w in self.pq:
			if w[1] == word:
				changed = w
				flag = True
		if flag:
			self.pq.remove(changed)
		heappush(self.pq, (self.dic[word], word))
		if len(self.pq) > self.k:
			heappop(self.pq)

	def getTopK(self,k):
		return [x[1] for x in self.pq]

m = Solution()
m.addWord("a")
m.addWord("b")
m.addWord("a")
m.addWord("e")
m.addWord("f")
m.addWord("c")
print m.getTopK(2)






		