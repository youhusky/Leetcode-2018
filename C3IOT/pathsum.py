# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # corner case
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        # O(n)
        res = []
        if not root:
            return res
        self.check(root, sum, res, [])
        return res
    
    def check(self, root, sum, res, temp):
        if not root:
            return
        if not root.left and not root.right and root.val == sum:
            res.append(list(temp+[root.val]))
        #print temp
        return self.check(root.left, sum - root.val, res, temp + [root.val]) or self.check(root.right, sum-root.val, res, temp+ [root.val])
        