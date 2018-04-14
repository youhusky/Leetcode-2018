#
# [89] Gray Code
#
# https://leetcode.com/problems/gray-code/description/
#
# algorithms
# Medium (42.44%)
# Total Accepted:    106K
# Total Submissions: 249.7K
# Testcase Example:  '2'
#
# The gray code is a binary numeral system where two successive values differ
# in only one bit.
# 
# Given a non-negative integer n representing the total number of bits in the
# code, print the sequence of gray code. A gray code sequence must begin with
# 0.
# 
# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
# 
# 
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# 
# 
# Note:
# For a given n, a gray code sequence is not uniquely defined.
# 
# For example, [0,2,3,1] is also a valid gray code sequence according to the
# above definition.
# 
# For now, the judge is able to judge based on one instance of gray code
# sequence. Sorry about that.
# 
#
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]

        """
        if n<1:
            return [0]
        if (n==1):
            return [0,1]
        res = self.grayCode( n-1)
        x=pow(2,n-1)
        for i in range(x-1,-1,-1):
            res.append(res[i]+x)
        return res
