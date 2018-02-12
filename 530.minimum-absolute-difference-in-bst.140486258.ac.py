#
# [530] Minimum Absolute Difference in BST
#
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (47.13%)
# Total Accepted:    31.8K
# Total Submissions: 67.5K
# Testcase Example:  '[1,null,3,2]'
#
# Given a binary search tree with non-negative values, find the minimum
# absolute difference between values of any two nodes.
# 
# 
# Example:
# 
# Input:
# 
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   /
# ⁠  2
# 
# Output:
# 1
# 
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1
# (or between 2 and 3).
# 
# 
# 
# 
# Note:
# There are at least two nodes in this BST.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # O(n)
        self.total = float('inf')
        self.helper(root, float('-inf'), float('inf'))
        return self.total
    
    def helper(self, root, left, right):
        if not root:
            return 
        self.total = min(self.total, (root.val - left), (right - root.val))
        self.helper(root.left, left, root.val)
        self.helper(root.right, root.val, right)
        
