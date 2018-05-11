class TrieNode(object):
    def __init__(self):
        self.children = dict()
        self.isEnd = False
        self.data = None
        
class AutocompleteSystem(object):

    def __init__(self, words):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.root = TrieNode()
        #self.keyword = ""
        for word in words:
            self.addRecord(word)
            
    def addRecord(self, word):
        p = self.root
        for char in word:
            char = char.lower()
            if char not in p.children:
                p.children[char] = TrieNode()
            p = p.children[char]
        p.isEnd = True   
        p.data = word
        
        
    def search(self, word):
        p = self.root
        for char in word:
            char = char.lower()
            if char not in p.children:
                return []
            p = p.children[char]
        return self.dfs(p)
    
    def dfs(self, root):
        res = []
        if root:
            # find the end
            if root.isEnd:
                res.append(root.data)
            for child in root.children:
                res.extend(self.dfs(root.children[child]))
        return res
    
    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        res = []
        if c != "#":
            self.keyword += c
            res = self.search(self.keyword)
        # else:
        #     self.addRecord(self.keyword,1)
        #     self.keyword = ""
        return res
        


# Your AutocompleteSystem object will be instantiated and called as such:
m = AutocompleteSystem(["ab",'ac','cd','ee','av'])
print m.search('a')


def build(word):
	dic = dict()
	for i in range(1, len(word)+1):
		dic[word[:i]] = word
	return dic
print build('apple')
