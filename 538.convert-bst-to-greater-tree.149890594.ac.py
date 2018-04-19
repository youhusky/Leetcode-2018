#
# [538] Convert BST to Greater Tree
#
# https://leetcode.com/problems/convert-bst-to-greater-tree/description/
#
# algorithms
# Easy (48.67%)
# Total Accepted:    40.4K
# Total Submissions: 83.1K
# Testcase Example:  '[5,2,13]'
#
# Given a Binary Search Tree (BST), convert it to a Greater Tree such that
# every key of the original BST is changed to the original key plus sum of all
# keys greater than the original key in BST.
# 
# 
# Example:
# 
# Input: The root of a Binary Search Tree like this:
# ⁠             5
# ⁠           /   \
# ⁠          2     13
# 
# Output: The root of a Greater Tree like this:
# ⁠            18
# ⁠           /   \
# ⁠         20     13
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def __init__(self):
#         self.total = 0
#     def convertBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: TreeNode
#         """
#         if root:
#             self.convertBST(root.right)
#             self.total += root.val
#             root.val = self.total
#             self.convertBST(root.left)
#         return root
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # iterative way
        total = 0
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
                
            node = stack.pop()
            total += node.val
            node.val = total
            node = node.left
            
        return root
        
        
