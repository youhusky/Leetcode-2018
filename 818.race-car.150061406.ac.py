#
# [836] Race Car
#
# https://leetcode.com/problems/race-car/description/
#
# algorithms
# Hard (25.18%)
# Total Accepted:    1.3K
# Total Submissions: 5K
# Testcase Example:  '3'
#
# Your car starts at position 0 and speed +1 on an infinite number line.  (Your
# car can go into negative positions.)
# 
# Your car drives automatically according to a sequence of instructions A
# (accelerate) and R (reverse).
# 
# When you get an instruction "A", your car does the following: position +=
# speed, speed *= 2.
# 
# When you get an instruction "R", your car does the following: if your speed
# is positive then speed = -1 , otherwise speed = 1.  (Your position stays the
# same.)
# 
# For example, after commands "AAR", your car goes to positions 0->1->3->3, and
# your speed goes to 1->2->4->-1.
# 
# Now for some target position, say the length of the shortest sequence of
# instructions to get there.
# 
# 
# Example 1:
# Input: 
# target = 3
# Output: 2
# Explanation: 
# The shortest instruction sequence is "AA".
# Your position goes from 0->1->3.
# 
# 
# 
# Example 2:
# Input: 
# target = 6
# Output: 5
# Explanation: 
# The shortest instruction sequence is "AAARA".
# Your position goes from 0->1->3->7->7->6.
# 
# 
# 
# 
# Note: 
# 
# 
# 1 <= target <= 10000.
# 
#
class Solution:
    def racecar(self, target):
        if target==0:
            return 0
        q = [(0, 1)]
        visited = set((0, 1))
        cnt = 0
        while q:
            new_q = []
            cnt += 1
            for pos, sp in q:
                # two ways
                
                p1, s1 = pos+sp, sp*2
                if p1==target:
                    return cnt
                
                p2, s2 = pos, -1 if sp>0 else 1
                
                # If we remember every position and speed pair, we get Memory Limit Exceed
                # The most annoying part is continuous R, so only remember situations with speed 1 and -1
                if (p1, s1) not in visited:
                    #visited.add((p2, s2))
                    new_q.append((p1, s1))
                if (p2, s2) not in visited:
                    visited.add((p2, s2))
                    # if s2==1 or s2==-1:
                    #     visited.add((p2, s2))
                    new_q.append((p2, s2))
            q = new_q
        return -1
