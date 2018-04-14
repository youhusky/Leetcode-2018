#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (49.52%)
# Total Accepted:    94.9K
# Total Submissions: 191.6K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# 
# Given a non-empty array of integers, return the k most frequent elements.
# 
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
# 
# 
# Note: 
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is
# the array's size.
# 
#
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        res = []
        pq = []
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        
        for key in dic:
            heapq.heappush(pq, (-dic[key], key))
            
        while k:
            res.append(heapq.heappop(pq)[1])
            k -= 1
        return res
            
        
