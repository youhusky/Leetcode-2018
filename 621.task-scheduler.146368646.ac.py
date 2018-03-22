#
# [621] Task Scheduler
#
# https://leetcode.com/problems/task-scheduler/description/
#
# algorithms
# Medium (42.52%)
# Total Accepted:    29.6K
# Total Submissions: 69.6K
# Testcase Example:  '["A","A","A","B","B","B"]\n2'
#
# Given a char array representing tasks CPU need to do. It contains capital
# letters A to Z where different letters represent different tasks.Tasks could
# be done without original order. Each task could be done in one interval. For
# each interval, CPU could finish one task or just be idle.
# 
# However, there is a non-negative cooling interval n that means between two
# same tasks, there must be at least n intervals that CPU are doing different
# tasks or just be idle. 
# 
# You need to return the least number of intervals the CPU will take to finish
# all the given tasks.
# 
# Example 1:
# 
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
# 
# 
# 
# Note:
# 
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].
# 
# 
#
from collections import defaultdict
class Solution(object):
    def leastInterval(self,tasks, n):

        dic = defaultdict(int)
        for task in tasks:
            dic[task] += 1
        maxvalue = max(dic.values())
        count = 0
        for key in dic:
            if dic[key] == maxvalue:
                count += 1
        partcnt = maxvalue -1
        partlen = n + 1 - count

        remain_plot = partcnt * partlen
        remain_item = len(tasks) - maxvalue * count
        remainappend = max(0, remain_plot- remain_item)
        return len(tasks) + remainappend
