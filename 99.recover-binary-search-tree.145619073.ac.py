#
# [99] Recover Binary Search Tree
#
# https://leetcode.com/problems/recover-binary-search-tree/description/
#
# algorithms
# Hard (30.96%)
# Total Accepted:    86.3K
# Total Submissions: 278.6K
# Testcase Example:  '[0,1]'
#
# 
# Two elements of a binary search tree (BST) are swapped by mistake.
# 
# Recover the tree without changing its structure.
# 
# 
# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a
# constant space solution?
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.first, self.second = None, None
        self.prev = TreeNode(float('-inf'))
        
        self.traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        
    def traverse(self, root):
        if not root:
            return
        self.traverse(root.left)
        if self.first == None and self.prev.val >= root.val:
            self.first = self.prev
        if self.first != None and self.prev.val >= root.val:
            self.second = root
        self.prev = root
        self.traverse(root.right)
        
