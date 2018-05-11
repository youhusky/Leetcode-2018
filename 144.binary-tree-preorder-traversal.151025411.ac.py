#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (46.39%)
# Total Accepted:    212.3K
# Total Submissions: 457.6K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the preorder traversal of its nodes' values.
# 
# 
# For example:
# Given binary tree [1,null,2,3],
# 
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# 
# 
# return [1,2,3].
# 
# 
# Note: Recursive solution is trivial, could you do it iteratively?
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.traverse(root, res)
        return res
    
    def traverse(self, root, res):
        if not root:
            return 
        
        res.append(root.val)
        self.traverse(root.left, res)
        self.traverse(root.right, res)
