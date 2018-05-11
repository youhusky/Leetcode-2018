#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (30.51%)
# Total Accepted:    103.8K
# Total Submissions: 340.2K
# Testcase Example:  '["Trie","search"]\n[[],["a"]]'
#
# 
# Implement a trie with insert, search, and startsWith methods.
# 
# 
# 
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
# 
#
from collections import defaultdict
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodes = [0 for _ in range(26)]   # Easy to insert new node.
        self.isword = False  # True for the end of the trie.
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for char in word:
            index = ord(char) - 97
            if curr.nodes[index] == 0:
                temp = TrieNode()
                curr.nodes[index] = temp
                curr = temp
            else:
                curr = curr.nodes[index]
        curr.isword = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for char in word:
            index = ord(char) - 97
            if curr.nodes[index] == 0:
                return False
            else:
                curr = curr.nodes[index]
        return curr.isword
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for char in prefix:
            index = ord(char) - 97
            if curr.nodes[index] == 0:
                return False
            else:
                curr = curr.nodes[index]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
