#
# [793] Swap Adjacent in LR String
#
# https://leetcode.com/problems/swap-adjacent-in-lr-string/description/
#
# algorithms
# Medium (26.49%)
# Total Accepted:    2.6K
# Total Submissions: 9.8K
# Testcase Example:  '"X"\n"L"'
#
# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a
# move consists of either replacing one occurrence of "XL" with "LX", or
# replacing one occurrence of "RX" with "XR". Given the starting string start
# and the ending string end, return True if and only if there exists a sequence
# of moves to transform one string to the other.
# 
# Example:
# 
# 
# Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
# Output: True
# Explanation:
# We can transform start to end following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
# 
# 
# Note:
# 
# 
# 1 <= len(start) = len(end) <= 10000.
# Both start and end will only consist of characters in {'L', 'R', 'X'}.
# 
#
class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if start.replace('X','')!=end.replace('X',''): return False
        print start,end
        l1=l2=r1=r2=0
        # XL -> LX and RX -> XR
        for v1,v2 in zip(start,end):
            if v1=='L': l1+=1
            elif v1=='R': r1+=1
            if v2=='L': l2+=1
            elif v2=='R': r2+=1
            if l1>l2 or r1<r2: return False
        return True
