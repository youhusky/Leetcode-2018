#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (48.84%)
# Total Accepted:    254.7K
# Total Submissions: 521.5K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
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
# return [1,3,2].
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
    def inorderTraversal(self, root):
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
        self.traverse(root.left, res)
        res.append(root.val)
        self.traverse(root.right, res)
        
