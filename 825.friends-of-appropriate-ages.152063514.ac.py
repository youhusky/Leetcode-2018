#
# [852] Friends Of Appropriate Ages
#
# https://leetcode.com/problems/friends-of-appropriate-ages/description/
#
# algorithms
# Medium (25.93%)
# Total Accepted:    2.8K
# Total Submissions: 10.7K
# Testcase Example:  '[16,16]'
#
# Some people will make friend requests. The list of their ages is given and
# ages[i] is the age of the ith person. 
# 
# Person A will NOT friend request person B (B != A) if any of the following
# conditions are true:
# 
# 
# age[B] <= 0.5 * age[A] + 7
# age[B] > age[A]
# age[B] > 100 && age[A] < 100
# 
# 
# Otherwise, A will friend request B.
# 
# Note that if A requests B, B does not necessarily request A.  Also, people
# will not friend request themselves.
# 
# How many total friend requests are made?
# 
# Example 1:
# 
# 
# Input: [16,16]
# Output: 2
# Explanation: 2 people friend request each other.
# 
# 
# Example 2:
# 
# 
# Input: [16,17,18]
# Output: 2
# Explanation: Friend requests are made 17 -> 16, 18 -> 17.
# 
# Example 3:
# 
# 
# Input: [20,30,100,110,120]
# Output: 
# Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 ->
# 100.
# 
# 
# 
# 
# Notes:
# 
# 
# 1 <= ages.length <= 20000.
# 1 <= ages[i] <= 120.
# 
#
class Solution(object):
    def numFriendRequests(self, ages):
        count = [0] * 121
        for age in ages:
            count[age] += 1

        ans = 0
        for ageA, countA in enumerate(count):
            for ageB, countB in enumerate(count):
                if ageA * 0.5 + 7 >= ageB: continue
                if ageA < ageB: continue
                if ageA < 100 < ageB: continue
                ans += countA * countB
                if ageA == ageB: ans -= countA

        return ans
