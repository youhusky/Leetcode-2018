#
# [652] Find Duplicate Subtrees
#
# https://leetcode.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (36.84%)
# Total Accepted:    13.1K
# Total Submissions: 35.4K
# Testcase Example:  '[2,1,1]'
#
# 
# Given a binary tree, return all duplicate subtrees. For each kind of
# duplicate subtrees, you only need to return the root node of any one of
# them. 
# 
# 
# Two trees are duplicate if they have the same structure with same node
# values.
# 
# 
# Example 1: 
# 
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   2   4
# ⁠      /
# ⁠     4
# 
# The following are two duplicate subtrees:
# 
# ⁠     2
# ⁠    /
# ⁠   4
# 
# and
# 
# ⁠   4
# 
# Therefore, you need to return above trees' root in the form of a list.
# 
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.dic = defaultdict(list)
        self.check(root)
        res = []
        #print self.dic
        for key in self.dic:
            if len(self.dic[key]) > 1:
                res.append(self.dic[key][0])
        return res
    
    def check(self, root):
        if not root:
            return "None"
        key  = "%s,%s,%s" % (str(root.val), self.check(root.left), self.check(root.right))
        self.dic[key].append(root)
        return key
               
