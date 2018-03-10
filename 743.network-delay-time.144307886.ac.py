#
# [744] Network Delay Time
#
# https://leetcode.com/problems/network-delay-time/description/
#
# algorithms
# Medium (34.27%)
# Total Accepted:    5.3K
# Total Submissions: 15.3K
# Testcase Example:  '[[2,1,1],[2,3,1],[3,4,1]]\n4\n2'
#
# 
# There are N network nodes, labelled 1 to N.
# 
# Given times, a list of travel times as directed edges times[i] = (u, v, w),
# where u is the source node, v is the target node, and w is the time it takes
# for a signal to travel from source to target.
# 
# Now, we send a signal from a certain node K.  How long will it take for all
# nodes to receive the signal?  If it is impossible, return -1.
# 
# 
# Note:
# 
# N will be in the range [1, 100].
# K will be in the range [1, N].
# The length of times will be in the range [1, 6000].
# All edges times[i] = (u, v, w) will have 1  and 1 .
# 
# 
#
import heapq
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        # Dijkstra's
        pq = [[0,K]]
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append([v,w])
            
        dic = dict()  
        
        while pq:
            distance, node = heapq.heappop(pq)
            if node in dic:
                continue
            dic[node] = distance
            for desination, path in graph[node]:
                if desination not in dic:
                    heapq.heappush(pq,(distance + path, desination))
        return max(dic.values()) if len(dic) == N else -1
