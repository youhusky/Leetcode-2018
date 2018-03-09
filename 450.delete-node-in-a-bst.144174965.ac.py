#
# [450] Delete Node in a BST
#
# https://leetcode.com/problems/delete-node-in-a-bst/description/
#
# algorithms
# Medium (37.63%)
# Total Accepted:    30.5K
# Total Submissions: 81.1K
# Testcase Example:  '[5,3,6,2,4,null,7]\n3'
#
# Given a root node reference of a BST and a key, delete the node with the
# given key in the BST. Return the root node reference (possibly updated) of
# the BST.
# 
# Basically, the deletion can be divided into two stages:
# 
# Search for a node to remove.
# If the node is found, delete the node.
# 
# 
# 
# Note: Time complexity should be O(height of tree).
# 
# Example:
# 
# root = [5,3,6,2,4,null,7]
# key = 3
# 
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
# 
# Given key to delete is 3. So we find the node with value 3 and delete it.
# 
# One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
# 
# ⁠   5
# ⁠  / \
# ⁠ 4   6
# ⁠/     \
# 2       7
# 
# Another valid answer is [5,2,6,null,4,null,7].
# 
# ⁠   5
# ⁠  / \
# ⁠ 2   6
# ⁠  \   \
# ⁠   4   7
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # case 1
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # find
            minNode = self.findmin(root.right)
            # delete
            print minNode.val
            root.val = minNode.val
            root.right = self.deleteNode(root.right, root.val)
        return root
        
        
    def findmin(self, root):
        while root.left:
            root = root.left
        return root
