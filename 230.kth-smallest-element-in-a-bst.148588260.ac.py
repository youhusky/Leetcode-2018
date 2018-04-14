#
# [230] Kth Smallest Element in a BST
#
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (45.08%)
# Total Accepted:    132.1K
# Total Submissions: 293K
# Testcase Example:  '[1]\n1'
#
# Given a binary search tree, write a function kthSmallest to find the kth
# smallest element in it.
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
# 
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to
# find the kth smallest frequently? How would you optimize the kthSmallest
# routine?
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.res = None
        self.helper(root)
        return self.res
    
    def helper(self, root):
        if not root:
            return 
        self.helper(root.left)
        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return 
        self.helper(root.right)
