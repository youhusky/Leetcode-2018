#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (40.61%)
# Total Accepted:    146.1K
# Total Submissions: 359.7K
# Testcase Example:  '[1,2,3,null,5]'
#
# 
# Given a binary tree, return all root-to-leaf paths.
# 
# 
# For example, given the following binary tree:
# 
# 
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# 
# 
# All root-to-leaf paths are:
# ["1->2->5", "1->3"]
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # O(n), O(h)
        res = []
        if not root:
            return res
        self.check(root, res, str(root.val))
        return res
    
    def check(self, root, res, temp):
        # corner case
        if not root:
            return
        # left node
        if not root.left and not root.right:
            res.append(temp)
            return
        if root.left:
            self.check(root.left, res, temp + '->' + str(root.left.val))
        if root.right:
            self.check(root.right, res, temp + '->' + str(root.right.val))
