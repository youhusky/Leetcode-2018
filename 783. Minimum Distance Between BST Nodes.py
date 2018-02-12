# Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

# Example :

# Input: root = [4,2,6,1,3,null,null]
# Output: 1
# Explanation:
# Note that root is a TreeNode object, not an array.

# The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

#           4
#         /   \
#       2      6
#      / \    
#     1   3  

# while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
# Note:

# The size of the BST will be between 2 and 100.
# The BST is always valid, each node's value is an integer, and each node's value is different.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
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
        