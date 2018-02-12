#
# [298] Binary Tree Longest Consecutive Sequence
#
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/description/
#
# algorithms
# Medium (41.64%)
# Total Accepted:    40.8K
# Total Submissions: 98K
# Testcase Example:  '[1,null,3,2,4,null,null,null,5]'
#
# 
# Given a binary tree, find the length of the longest consecutive sequence
# path.
# 
# 
# The path refers to any sequence of nodes from some starting node to any node
# in the tree along the parent-child connections. The longest consecutive path
# need to be from parent to child (cannot be the reverse).
# 
# 
# 
# For example,
# 
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   / \
# ⁠  2   4
# ⁠       \
# ⁠        5
# 
# Longest consecutive sequence path is 3-4-5, so return 3. 
# 
# ⁠  2
# ⁠   \
# ⁠    3
# ⁠   / 
# ⁠  2    
# ⁠ / 
# ⁠1
# 
# Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
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
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.total = 1
        
        self.helper(root, root.val, 0)
        return self.total
    
    def helper(self, root, target, cur):
        if not root:
            return
        if root.val == target:
            cur += 1
        else:
            cur = 1
        self.total = max(self.total, cur)
        self.helper(root.left, root.val+1 , cur)
        self.helper(root.right, root.val+1, cur)
        
        
