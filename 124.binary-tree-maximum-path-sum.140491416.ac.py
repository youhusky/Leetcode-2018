#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (26.96%)
# Total Accepted:    119.4K
# Total Submissions: 442.7K
# Testcase Example:  '[1,2,3]'
#
# 
# Given a binary tree, find the maximum path sum.
# 
# 
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
# 
# 
# For example:
# Given the below binary tree,
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# 
# 
# Return 6.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # O(n), O(lgn)
        self.total = float('-inf')
        self.helper(root)
        return self.total
    
    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        # three case can return parent
        temp = max(root.val + left, root.val + right, root.val)
        # three case that cause
        self.total = max(self.total, root.val+left+right, temp)
        return temp
