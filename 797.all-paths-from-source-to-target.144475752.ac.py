#
# [813] All Paths From Source to Target
#
# https://leetcode.com/problems/all-paths-from-source-to-target/description/
#
# algorithms
# Medium (73.71%)
# Total Accepted:    1.2K
# Total Submissions: 1.7K
# Testcase Example:  '[[1,2],[3],[3],[]]'
#
# Given a directed, acyclic graph of N nodes.  Find all possible paths from
# node 0 to node N-1, and return them in any order.
# 
# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.
# graph[i] is a list of all nodes j for which the edge (i, j) exists.
# 
# 
# Example:
# Input: [[1,2], [3], [3], []] 
# Output: [[0,1,3],[0,2,3]] 
# Explanation: The graph looks like this:
# 0--->1
# |    |
# v    v
# 2--->3
# There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
# 
# 
# Note:
# 
# 
# The number of nodes in the graph will be in the range [2, 15].
# You can print different paths in any order, but you should keep the order of
# nodes inside one path.
# 
# 
#
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        
        res = []
        dic = collections.defaultdict(list)
        for index in range(len(graph)-1):
            if len(graph[index]) > 1:
                for each in graph[index]:
                    #print each
                    dic[each].append(index)
            else:
                dic[graph[index][0]].append(index)
                
        def dfs(node, temp):
            if temp and temp[-1] == 0:
                res.append((list(temp[::-1])))
                return
            for n in dic[node]:
                temp.append(n)
                dfs(n,temp)
                temp.pop()
        dfs(len(graph)-1, [len(graph)-1])
        return res
