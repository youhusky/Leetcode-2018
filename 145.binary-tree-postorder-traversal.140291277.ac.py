#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (41.45%)
# Total Accepted:    167K
# Total Submissions: 402.8K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the postorder traversal of its nodes' values.
# 
# For example:
# Given binary tree [1,null,2,3],
# 
# 
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# 
# 
# 
# return [3,2,1].
# 
# Note: Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
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
        self.traverse(root.right, res)
        res.append(root.val)
