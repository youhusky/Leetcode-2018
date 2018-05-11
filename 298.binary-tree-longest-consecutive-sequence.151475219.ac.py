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
        res = 1
        queue = [(root,1)]
        
        while queue:
            size = len(queue)
            while size:
                
                node,length = queue.pop(0)
                
                res = max(res, length)
                if node.left:
                    if node.left.val == node.val+1:
                        queue.append((node.left, length+1))
                    else:
                        queue.append((node.left, 1))
                    
                if node.right:
                    if node.right.val == node.val+1:
                        queue.append((node.right, length+1))
                    else:
                        queue.append((node.right, 1))
                    
                size -= 1
        return res
        
