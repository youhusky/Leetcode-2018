#
# [337] House Robber III
#
# https://leetcode.com/problems/house-robber-iii/description/
#
# algorithms
# Medium (44.73%)
# Total Accepted:    63.4K
# Total Submissions: 141.8K
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
# 
# The thief has found himself a new place for his thievery again. There is only
# one entrance to this area, called the "root." Besides the root, each house
# has one and only one parent house. After a tour, the smart thief realized
# that "all houses in this place forms a binary tree". It will automatically
# contact the police if two directly-linked houses were broken into on the same
# night.
# 
# 
# 
# Determine the maximum amount of money the thief can rob tonight without
# alerting the police.
# 
# 
# Example 1:
# 
# ⁠    3
# ⁠   / \
# ⁠  2   3
# ⁠   \   \ 
# ⁠    3   1
# 
# Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# 
# 
# Example 2:
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \   \ 
# ⁠1   3   1
# 
# Maximum amount of money the thief can rob = 4 + 5 = 9.
# 
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0,0]
        return max(self.dfs(root, res))
        
    
    def dfs(self, root, res):
        if not root:
            return [0,0]
        left = self.dfs(root.left, res)
        right = self.dfs(root.right, res)
        res = [0,0]
        # res[0] not robor
        # res[1] robor
        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = root.val + left[0] + right[0]
        return res
        
