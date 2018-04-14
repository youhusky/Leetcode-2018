#
# [275] H-Index II
#
# https://leetcode.com/problems/h-index-ii/description/
#
# algorithms
# Medium (34.88%)
# Total Accepted:    61.5K
# Total Submissions: 176.4K
# Testcase Example:  '[]'
#
# 
# Follow up for H-Index: What if the citations array is sorted in ascending
# order? Could you optimize your algorithm?
# 
#
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        low, high = 0, N - 1
        while low <= high:
            mid = (low + high) / 2
            if N - mid > citations[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return N - low
