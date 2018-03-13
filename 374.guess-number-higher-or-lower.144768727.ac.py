#
# [374] Guess Number Higher or Lower
#
# https://leetcode.com/problems/guess-number-higher-or-lower/description/
#
# algorithms
# Easy (36.53%)
# Total Accepted:    68.6K
# Total Submissions: 187.8K
# Testcase Example:  '10\n6'
#
# We are playing the Guess Game. The game is as follows: 
# 
# I pick a number from 1 to n. You have to guess which number I picked.
# 
# Every time you guess wrong, I'll tell you whether the number is higher or
# lower.
# 
# You call a pre-defined API guess(int num) which returns 3 possible results
# (-1, 1, or 0):
# 
# -1 : My number is lower
# ⁠1 : My number is higher
# ⁠0 : Congrats! You got it!
# 
# 
# Example:
# 
# n = 10, I pick 6.
# 
# Return 6.
# 
# 
#
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,r = 1,n
        while l + 1 < r:
            mid = l + (r-l)/2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                l = mid
            else:
                r = mid
        return l if guess(l) == 0 else r
