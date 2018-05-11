class Friendship(object):
	"""docstring for Friendship"""
	def __init__(self):
		super(Friendship, self).__init__()
		self.friendship = dict()
		
	def makeFriend(self, name1, name2):
		# check
		if not name1 or not name2:
			print "Error"
			return
		self.friendship[name1] = self.friendship.get(name1, []) + [name2]
		self.friendship[name2] = self.friendship.get(name2, []) + [name1]
		


	def unmakeFriend(self, name1, name2):
		if not name1 or not name2:
			print "Error"
			return

		if name1 not in self.friendship or name2 not in self.friendship:
			print "Error"
			return
		self.friendship[name1].remove(name2)
		self.friendship[name2].remove(name1)

	def getDirectFriend(self, name):
		if not name:
			print "Error"
			return
		return self.friendship.get(name)

	def getInDirectFriend(self, name):
		if not name:
			print "Error"
			return
		indirectfriend = []
		indirectfriend.append(name)
		indirectfriend = self.helper(name, indirectfriend)
		indirectfriend.remove(name)
		myfriend = self.friendship.get(name)
		for f in myfriend:
			if f in indirectfriend:
				indirectfriend.remove(f)

		return indirectfriend

	def helper(self, name, totalfriend):
		directfriend = self.friendship.get(name)
		for f in directfriend:
			if f not in totalfriend:
				totalfriend.append(f)
				self.helper(f, totalfriend)
		return totalfriend


f = Friendship()
f.makeFriend("A","B")
f.makeFriend("B","C")
f.makeFriend("B","D")
f.makeFriend("D","E")
f.makeFriend("C","F")
print "C.direct"
print f.getDirectFriend("C")
print "C.indirect"
print f.getInDirectFriend("C")

		
