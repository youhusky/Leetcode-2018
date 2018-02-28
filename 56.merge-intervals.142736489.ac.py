#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (31.74%)
# Total Accepted:    183.6K
# Total Submissions: 578.3K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# 
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].
# 
#
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 2:
            return intervals
        intervals = sorted(intervals, key = lambda x:x.start)
        res = []
        start = intervals[0].start
        end = intervals[0].end
        for interval in intervals:
            if interval.start <= end:
                end = max(end, interval.end) # [1,10], [2,5]
            else:
                res.append(Interval(start, end))
                start = interval.start
                end = interval.end
        # the last one
        res.append(Interval(start, end))
        return res
            
        
        
