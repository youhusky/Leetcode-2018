#
# [809] Preimage Size of Factorial Zeroes Function
#
# https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/description/
#
# algorithms
# Hard (29.97%)
# Total Accepted:    359
# Total Submissions: 1.2K
# Testcase Example:  '0'
#
# Let f(x) be the number of zeroes at the end of x!. (Recall that x! = 1 * 2 *
# 3 * ... * x, and by convention, 0! = 1.)
# 
# For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while f(11) =
# 2 because 11! = 39916800 has 2 zeroes at the end. Given K, find how many
# non-negative integers x have the property that f(x) = K.
# 
# 
# Example 1:
# Input: K = 0
# Output: 5
# Explanation: 0!, 1!, 2!, 3!, and 4! end with K = 0 zeroes.
# 
# Example 2:
# Input: K = 5
# Output: 0
# Explanation: There is no x such that x! ends in K = 5 zeroes.
# 
# 
# Note:
# 
# 
# K will be an integer in the range [0, 10^9].
# 
#
class Solution(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        # 数学题，确定有多少个数字后面带K个0
        n = 4*K
        count = 0
        while n!=0:
            count += n/5
            n/=5
        n = 4*K
        print count
        while count<K:
            n+=1
            t = n
            while t%5==0:
                count += 1
                t/=5
        print count
        if count>K:
            return 0
        else:
            return 5
