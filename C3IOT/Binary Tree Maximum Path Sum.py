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
        total = float('-inf')
        self.helper(root,total)
        return total
    
    def helper(self, root, total):
        if not root:
            return 0
        left = self.helper(root.left,total)
        right = self.helper(root.right,total)
        # three case can return parent
        temp = max(root.val + left, root.val + right, root.val)
        # three case that cause
        total = max(total, root.val+left+right, temp)
        return temp