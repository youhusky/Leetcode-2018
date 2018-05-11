class Friend(object):
	"""docstring for Friend"""
	def __init__(self, name):
		super(Friend, self).__init__()
		self.name = name
		self.friends = []

	def __repr__(self):
		return self.name

	def makeFriend(self, friend):
		if not friend:
			print "Empty input"
		if friend not in self.friends:
			self.friends.append(friend)
		if self not in friend.friends:
			friend.friends.append(self)

	def unmakeFriend(self, friend):
		if not friend:
			print "Empty input"
		if friend in self.friends:
			self.friends.remove(friend)
		if self in friend.friends:
			friend.friends.remove(self)

	def getDirectFriend(self):
		return self.friends

	def getInDirectFriend(self):
		temp = []
		temp.append(self)
		temp = self.getInDirectFriendHelper(self, temp)
		temp.remove(self)
		for indirectfriend in temp:
			if indirectfriend in self.friends:
				temp.remove(indirectfriend)
		return temp


	def getInDirectFriendHelper(self, friend, temp):
		for directfriend in friend.friends:
			if directfriend not in temp:
				temp.append(directfriend)
				self.getInDirectFriendHelper(directfriend, temp)
		return temp


f1 = Friend("f1")
f2 = Friend("f2")
f3 = Friend("f3")
f4 = Friend("f4")
f5 = Friend("f5")

f1.makeFriend(f2)
f2.makeFriend(f3)
f3.makeFriend(f4)
f3.makeFriend(f5)

print "direct friend for f1"
print f1.getDirectFriend()
print "indirect friend for f1"
print f1.getInDirectFriend()
f1.unmakeFriend(f2)
print f1.getDirectFriend()
print f1.getInDirectFriend()
		