#
# [687] Longest Univalue Path
#
# https://leetcode.com/problems/longest-univalue-path/description/
#
# algorithms
# Easy (33.15%)
# Total Accepted:    19.3K
# Total Submissions: 58.2K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# Given a binary tree, find the length of the longest path where each node in
# the path has the same value. This path may or may not pass through the root.
# 
# Note: The length of path between two nodes is represented by the number of
# edges between them.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input:
# 
# ⁠             5
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         1   1   5
# 
# 
# 
# 
# Output:
# 
# 2
# 
# 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input:
# 
# ⁠             1
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         4   4   5
# 
# 
# 
# 
# Output:
# 
# 2
# 
# 
# 
# Note:
# The given binary tree has not more than 10000 nodes.  The height of the tree
# is not more than 1000.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        self.longest = 0
        self.traverse(root)
        return self.longest
        
    def traverse(self, node):
        if not node:
            return 0
        left_len, right_len = self.traverse(node.left), self.traverse(node.right)
        left = (left_len + 1) if node.left and node.left.val == node.val else 0
        right = (right_len + 1) if node.right and node.right.val == node.val else 0
        self.longest = max(self.longest, left + right)
        return max(left, right)

        
