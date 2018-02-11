#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (35.16%)
# Total Accepted:    154.2K
# Total Submissions: 438.6K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 
# Given a binary tree and a sum, find all root-to-leaf paths where each path's
# sum equals the given sum.
# 
# 
# For example:
# Given the below binary tree and sum = 22,
# 
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \    / \
# ⁠       7    2  5   1
# 
# 
# 
# return
# 
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
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
        
