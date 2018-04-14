def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        m = len(haystack) 
        n = len(needle) 
        for i in range(m):
            if i+n <= m:
                if haystack[i:i+n] == needle:
                    return True
        return False
def wordladder(start, dic):
	# dic = ['chat','hat','chats',bat']
	# start = 'at'
	# T O(n*mn)
	queue = [start]
	vis = set()
	while queue:
		word = queue.pop(0)

		candidate_length = len(word)+1
		for each in dic:
			#if len(each) == candidate_length and strStr(each,word) and each not in vis:
			if len(each) == candidate_length and word in each and each not in vis:
				queue.append(each)
				vis.add(each)
	return len(word)
dic = ['chat','hat','chats','bat']
start = 'at'
print(wordladder(start, dic))