#
# [842] Card Flipping Game
#
# https://leetcode.com/problems/card-flipping-game/description/
#
# algorithms
# Medium (34.03%)
# Total Accepted:    2.3K
# Total Submissions: 6.8K
# Testcase Example:  '[1,2,4,4,7]\n[1,3,4,1,3]'
#
# On a table are N cards, with a positive integer printed on the front and back
# of each card (possibly different).
# 
# We flip any number of cards, and after we choose one card. 
# 
# If the number X on the back of the chosen card is not on the front of any
# card, then this number X is good.
# 
# What is the smallest number that is good?  If no number is good, output 0.
# 
# Here, fronts[i] and backs[i] represent the number on the front and back of
# card i. 
# 
# A flip swaps the front and back numbers, so the value on the front is now on
# the back and vice versa.
# 
# Example:
# 
# 
# Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
# Output: 2
# Explanation: If we flip the second card, the fronts are [1,3,4,4,7] and the
# backs are [1,2,4,1,3].
# We choose the second card, which has number 2 on the back, and it isn't on
# the front of any card, so 2 is good.
# 
# 
# 
# Note:
# 
# 
# 1 <= fronts.length == backs.length <= 1000.
# 1 <= fronts[i] <= 2000.
# 1 <= backs[i] <= 2000.
# 
# 
#
class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        s = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                s.add(fronts[i])
        res = float('inf')
        for i in range(len(fronts)):
            if fronts[i] not in s:
                res = min(res, fronts[i])
            if backs[i] not in s:
                res = min(res, backs[i])
        return res if res != float('inf') else 0
        
