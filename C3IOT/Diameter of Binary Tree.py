# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # find depth
        self.res = 1
        self.traverse(root)
        return self.res - 1
    
    def traverse(self, root):
        if not root:
            return 0
        l = self.traverse(root.left)
        r = self.traverse(root.right)
        self.res = max(self.res, l+r + 1)
        return max(l, r) + 1
        