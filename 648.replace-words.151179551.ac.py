#
# [648] Replace Words
#
# https://leetcode.com/problems/replace-words/description/
#
# algorithms
# Medium (47.61%)
# Total Accepted:    14.5K
# Total Submissions: 30.6K
# Testcase Example:  '["cat", "bat", "rat"]\n"the cattle was rattled by the battery"'
#
# 
# In English, we have a concept called root, which can be followed by some
# other words to form another longer word - let's call this word successor. For
# example, the root an, followed by other, which can form another word
# another.
# 
# 
# 
# 
# Now, given a dictionary consisting of many roots and a sentence. You need to
# replace all the successor in the sentence with the root forming it. If a
# successor has many roots can form it, replace it with the root with the
# shortest length.
# 
# 
# 
# You need to output the sentence after the replacement.
# 
# 
# 
# Example 1:
# 
# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
# 
# 
# 
# 
# Note:
# 
# The input will only have lower-case letters.
# ⁠1 
# ⁠1 
# ⁠1 
# ⁠1 
# 
# 
#
class TrieNode:
    
    def __init__(self):
        self.root = dict()
    
    def insert(self, root):
        node = self.root
        
        for char in root:
            if char not in node:
                node[char] = dict()
            node = node[char]
        node['#'] = root
            
    def replace(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return word
            node = node[char]
            if node.get('#'):
                return node['#']
        return word


class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """

        trie = TrieNode()
        for root in dict:
            trie.insert(root)
            
        strs = sentence.split()
        for i,v in enumerate(strs):
            strs[i] = trie.replace(v)
        return " ".join(strs)
        
