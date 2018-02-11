#
# [129] Sum Root to Leaf Numbers
#
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
#
# algorithms
# Medium (37.50%)
# Total Accepted:    129.2K
# Total Submissions: 344.5K
# Testcase Example:  '[]'
#
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path
# could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# 
# Find the total sum of all root-to-leaf numbers.
# 
# For example,
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# 
# 
# 
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# 
# 
# Return the sum = 12 + 13 = 25.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.total = 0
        if not root:
            return 0
        self.helper(root, 0)
        return self.total
    
    def helper(self, root, total):
        
        if not root:
            return 0
        if not root.left and not root.right:
            self.total += total* 10 + root.val
        left = self.helper(root.left, total*10 + root.val)
        right = self.helper(root.right, total * 10 + root.val)
        return left + right
        
