#
# [211] Add and Search Word - Data structure design
#
# https://leetcode.com/problems/add-and-search-word-data-structure-design/description/
#
# algorithms
# Medium (24.99%)
# Total Accepted:    71.7K
# Total Submissions: 287.1K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# 
# Design a data structure that supports the following two operations:
# 
# 
# void addWord(word)
# bool search(word)
# 
# 
# 
# search(word) can search a literal word or a regular expression string
# containing only letters a-z or .. A . means it can represent any one
# letter.
# 
# 
# For example:
# 
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# 
# 
# 
# Note:
# You may assume that all words are consist of lowercase letters a-z.
# 
# 
# click to show hint.
# 
# You should be familiar with how a Trie works. If not, please work on this
# problem: Implement Trie (Prefix Tree) first.
# 
#
from collections import defaultdict
class TrieNode(object):
    def __init__(self):
        self.node = defaultdict(TrieNode)
        self.isWord = False

    def __repr__(self):
        return repr(self.node)
        
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for char in word:
            curr = curr.node[char]
        curr.isWord = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.find(self.root, word)
    
    def find(self, trie, word):
        if word == '':
            return trie.isWord
        
        if word[0] == '.':
            for i in trie.node:
                if self.find(trie.node[i], word[1:]):
                    return True
        else:
            child = trie.node.get(word[0])
            if child:
                return self.find(child, word[1:])
        return False
