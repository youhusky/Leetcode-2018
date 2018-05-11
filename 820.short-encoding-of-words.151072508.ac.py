#
# [839] Short Encoding of Words
#
# https://leetcode.com/problems/short-encoding-of-words/description/
#
# algorithms
# Medium (40.32%)
# Total Accepted:    2.7K
# Total Submissions: 6.7K
# Testcase Example:  '["time", "me", "bell"]'
#
# Given a list of words, we may encode it by writing a reference string S and a
# list of indexes A.
# 
# For example, if the list of words is ["time", "me", "bell"], we can write it
# as S = "time#bell#" and indexes = [0, 2, 5].
# 
# Then for each index, we will recover the word by reading from the reference
# string from that index until we reach a "#" character.
# 
# What is the length of the shortest reference string S possible that encodes
# the given words?
# 
# Example:
# 
# 
# Input: words = ["time", "me", "bell"]
# Output: 10
# Explanation: S = "time#bell#" and indexes = [0, 2, 5].
# 
# 
# Note:
# 
# 
# 1 <= words.length <= 2000.
# 1 <= words[i].length <= 7.
# Each word has only lowercase letters.
# 
# 
#
class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # build Trie
        trie = dict()
        for word in words:
            t = trie
            for w in reversed(word):
                if w not in t:
                    t[w] = dict()
                t = t[w]
            
        
        # search Trie
        height = 1
        queue = [trie]
 
        res = []
     
        
        while queue:
            size = len(queue)
            while size:
                node = queue.pop(0)
                for child in node:
                    if not node[child]:
                        res.append(height+1)
                    else:
                        queue.append(node[child])
                size -= 1
            
            height += 1
   
        return sum(res)
            
        
