class Rabbit(object):
	def __init__(self,x):
		self.val = x
		self.parent = []

class Solution(object):
	def findAncestor(self, rabbit1, rabbit2):
		queue = []
		queue.append(rabbit1)
		queue.append(rabbit2)
		visit = set()
		visit.add(rabbit1)
		visit.add(rabbit2)
		while queue:
			rabbit = queue.pop(0)
			for parent in rabbit.parent:
				queue.append(parent)
				if parent in visit:
					return parent.val
				visit.add(parent)
		return []
a = Rabbit(1)
b = Rabbit(2)
c = Rabbit(3)
d = Rabbit(4)
a.parent = [b]
b.parent = [c,d]
d.parent = [c]

m = Solution()
print m.findAncestor(a,d)

