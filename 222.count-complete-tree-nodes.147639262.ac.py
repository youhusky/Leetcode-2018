#
# [222] Count Complete Tree Nodes
#
# https://leetcode.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (27.71%)
# Total Accepted:    76.3K
# Total Submissions: 275.4K
# Testcase Example:  '[]'
#
# Given a complete binary tree, count the number of nodes.
# 
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is
# completely filled, and all nodes in the last level are as far left as
# possible. It can have between 1 and 2h nodes inclusive at the last level h.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # O(logn logn)
        h = self.height(root)
        nodes = 0
        while root:
            if self.height(root.right) == h - 1:
                nodes += 2 ** (h-1)  # left half (2 ** h - 1) and the root (1)
                root = root.right
            else:
                nodes += 2 ** (h - 2)
                root = root.left
            print nodes, h
            h -= 1
        return nodes        

    def height(self, root):
        return 0 if not root else 1 + self.height(root.left)
