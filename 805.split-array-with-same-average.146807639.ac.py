#
# [823] Split Array With Same Average
#
# https://leetcode.com/problems/split-array-with-same-average/description/
#
# algorithms
# Hard (19.77%)
# Total Accepted:    2K
# Total Submissions: 10.4K
# Testcase Example:  '[1,2,3,4,5,6,7,8]'
#
# In a given integer array A, we must move every element of A to either list B
# or list C. (B and C initially start empty.)
# 
# Return true if and only if after such a move, it is possible that the average
# value of B is equal to the average value of C, and B and C are both
# non-empty.
# 
# 
# Example :
# Input: 
# [1,2,3,4,5,6,7,8]
# Output: true
# Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of
# them have the average of 4.5.
# 
# 
# Note:
# 
# 
# The length of A will be in the range [1, 30].
# A[i] will be in the range of [0, 10000].
# 
# 
# 
# 
#
class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        res = []
        s = sum(A)
        avg = sum(A) / float(len(A))
        dic = dict()
        res = 0
        for i in range(1, len(A)):
            s = i *avg
            # int
            if abs(s - math.floor(s)) < 0.001 or abs(s - math.ceil(s)) < 0.0001:
                dic[int(s)]= i
                res = int(s)

        return self.backtracking(A, dic, 0, 0,0, res)
  
    def backtracking(self, A,dic, index, cur, count, res):
        if cur > res or index == len(A):
            return False
        if cur in dic and dic[cur] == count:
            return True
        for i in range(index, len(A)):
            exist = self.backtracking(A, dic, i+1, cur + A[i], count + 1, res)
            if exist:
                return True
        return False
            
            
        
        
