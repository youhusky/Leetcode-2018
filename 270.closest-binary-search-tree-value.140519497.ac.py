#
# [270] Closest Binary Search Tree Value
#
# https://leetcode.com/problems/closest-binary-search-tree-value/description/
#
# algorithms
# Easy (40.47%)
# Total Accepted:    46.5K
# Total Submissions: 114.8K
# Testcase Example:  '[1]\n4.428571'
#
# 
# Given a non-empty binary search tree and a target value, find the value in
# the BST that is closest to the target.
# 
# Note:
# 
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest
# to the target.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        r = root.val
        while root:
            if abs(root.val - target) < abs(r - target):
                r = root.val
            root = root.left if target < root.val else root.right
        return r
