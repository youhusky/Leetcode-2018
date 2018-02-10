#
# [323] Number of Connected Components in an Undirected Graph
#
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
#
# algorithms
# Medium (48.77%)
# Total Accepted:    33.9K
# Total Submissions: 69.4K
# Testcase Example:  '5\n[[0,1],[1,2],[3,4]]'
#
# 
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each
# edge is a pair of nodes), write a function to find the number of connected
# components in an undirected graph.
# 
# 
# 
# ⁠   Example 1:
# 
# 
# ⁠    0          3
# ⁠    |          |
# ⁠    1 --- 2    4
# 
# 
# ⁠   Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.
# 
# 
# ⁠   Example 2:
# 
# 
# ⁠    0           4
# ⁠    |           |
# ⁠    1 --- 2 --- 3
# 
# 
# ⁠   Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.
# 
# 
# 
# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges
# are undirected, [0, 1] is the same as [1, 0] and thus will not appear
# together in edges.
# 
#
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        # init
        count = n
        group = [i for i in range(n)]
        
        for e1, e2 in edges:
            root1 = self.find(e1, group)
            root2 = self.find(e2, group)
            if root1 == root2:
                pass
            else:
                count -= 1
                group[root2] = root1
                
        return count
            
    def find(self, e, group):
        if e == group[e]:
            return e
        else:
            return self.find(group[e], group)
        
