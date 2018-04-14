#
# [833] Bus Routes
#
# https://leetcode.com/problems/bus-routes/description/
#
# algorithms
# Hard (30.30%)
# Total Accepted:    1.8K
# Total Submissions: 6K
# Testcase Example:  '[[1,2,7],[3,6,7]]\n1\n6'
#
# We have a list of bus routes. Each routes[i] is a bus route that the i-th bus
# repeats forever. For example if routes[0] = [1, 5, 7], this means that the
# first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->...
# forever.
# 
# We start at bus stop S (initially not on a bus), and we want to go to bus
# stop T. Travelling by buses only, what is the least number of buses we must
# take to reach our destination? Return -1 if it is not possible.
# 
# 
# Example:
# Input: 
# routes = [[1, 2, 7], [3, 6, 7]]
# S = 1
# T = 6
# Output: 2
# Explanation: 
# The best strategy is take the first bus to the bus stop 7, then take the
# second bus to the bus stop 6.
# 
# 
# Note: 
# 
# 
# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 500.
# 0 <= routes[i][j] < 10 ^ 6.
# 
#
class Solution:
    def numBusesToDestination(self, routes, S, T):
        if S == T:
            return 0
        vistedBus = set()
        visitedStop = set()
        busToStop = collections.defaultdict(list)
        for i,route in enumerate(routes):
            for stop in route:
                busToStop[stop].append(i)
        front = {S}
        back = {T}
        visitedStop.add(S)
        visitedStop.add(T)
        distance = 1
        while front:
            newfront = set()
            for stop in front:
                for bus in busToStop[stop]:
                    if bus not in vistedBus:
                        vistedBus.add(bus)
                        for nextstop in routes[bus]:
                            if nextstop in back:
                                return distance
                            if nextstop not in visitedStop:
                                newfront.add(nextstop)
            distance += 1
            front = newfront
            visitedStop.update(front)
            if len(front) > len(back):
                front,back = back,front
        return -1
