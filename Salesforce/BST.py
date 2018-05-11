# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 问了几种算法，recursive, DFS, BFS
# DFS 和 BFS 区别，哪种比较好。  (DFS, BFS区别不大，因为要遍历所有节点，但是如果树很大， BFS is better， 可以 map reduce)
# -google 1point3acres
# 最后让写了recursive的code.


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

class Solution_iterative:
    def maxDepth(self, root):
        stack = [(root, 1)]
        total = 0
        while stack:
            node, depth = stack.pop()
            if node:
                total = max(total, depth)
                stack.extend([(node.left, depth + 1), (node.right, depth + 1)])
        return total
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
        temp = [root.val]
        self.check(root, res, temp)
        return res
    
    def check(self, root, res, temp):
        # corner case
        if not root:
            return
        # left node
        if not root.left and not root.right:
            res.append(list(temp))
            return
        
        if root.left:
            #self.check(root.left, res, temp + '->' + str(root.left.val))
            temp.append(root.left.val)
            self.check(root.left, res, temp)
            temp.pop()
        if root.right:
            print root.right.val,temp
            #self.check(root.right, res, temp + '->' + str(root.right.val))
            temp.append(root.right.val)
            self.check(root.right, res, temp)
            temp.pop()