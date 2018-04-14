#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (24.74%)
# Total Accepted:    63.3K
# Total Submissions: 255.7K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n["oath","pea","eat","rain"]'
#
# 
# Given a 2D board and a list of words from the dictionary, find all words in
# the board.
# 
# 
# Each word must be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring. The
# same letter cell may not be used more than once in a word.
# 
# 
# 
# For example,
# Given words = ["oath","pea","eat","rain"] and board = 
# 
# [
# ⁠ ['o','a','a','n'],
# ⁠ ['e','t','a','e'],
# ⁠ ['i','h','k','r'],
# ⁠ ['i','f','l','v']
# ]
# 
# 
# Return ["eat","oath"].
# 
# 
# 
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
# 
# 
# click to show hint.
# 
# You would need to optimize your backtracking to pass the larger test. Could
# you stop backtracking earlier?
# 
# If the current candidate does not exist in all words' prefix, you could stop
# backtracking immediately. What kind of data structure could answer such query
# efficiently? Does a hash table work? Why or why not? How about a Trie? If you
# would like to learn how to implement a basic trie, please work on this
# problem: Implement Trie (Prefix Tree) first.
# 
#
class Solution(object):
    def findWords(self, board, words):
        trie = {}
        for w in words:
            t = trie
            for c in w:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = '#'
        
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.find(board, i, j, trie, '', res)
        return list(set(res))

    def find(self, board, i, j, trie, path, res):
        # we find
        if '#' in trie:
            res.append(path)
        # not legal
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j] not in trie:
            return
        tmp = board[i][j]
        board[i][j] ="@"
        self.find(board, i+1, j, trie[tmp], path+tmp, res)
        self.find(board, i, j+1, trie[tmp], path+tmp, res)
        self.find(board, i-1, j, trie[tmp], path+tmp, res)
        self.find(board, i, j-1, trie[tmp], path+tmp, res)
        board[i][j] = tmp
