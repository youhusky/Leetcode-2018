# For example,
# Given "egg", "add", return true.

# Given "foo", "bar", return false.

# Given "paper", "title", return true.

class Solution(object):
	def __init__(self):
		self.Trie = dict()
	def printTrie(self):
		print self.Trie
	def regenerate_word(self,word):
		res = ""
		dic = dict()
		count = 0
		for c in word:
			if c not in dic:
				char = chr(97 + count)
				dic[c] = char
				res += char
				count += 1
			else:
				res += dic[c]
		return res

	def buildTrie(self,words):
		for word in words:
			t = self.Trie
			for w in self.regenerate_word(word):
				if w not in t:
					t[w] = dict()
				t = t[w]
			# end
			t['#'] = '#'
		return
	def check(self,s):
		t = self.Trie
		for w in self.regenerate_word(s):
			if w not in t:
				return False
			else:
				t = t[w]
		return t.get('#') == '#'
m = Solution()
m.buildTrie(["egg","tre"])
m.check("abc")
print m.printTrie()
print m.check("abc")
