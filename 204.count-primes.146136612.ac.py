#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (26.54%)
# Total Accepted:    149.2K
# Total Submissions: 562.1K
# Testcase Example:  '0'
#
# Description:
# Count the number of prime numbers less than a non-negative number, n.
# 
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
#
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return 0
        vis = [False] * n
        # sqrt
        for i in range(2, int(n ** 0.5) + 1):
            # not prime
            if vis[i]: continue
            j = i
            while j * i < n:
                vis[j * i] = True
                j += 1
        ans = 0
        for i in range(2, n):
            if not vis[i]: ans += 1
        return ans
