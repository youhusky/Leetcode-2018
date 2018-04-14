#
# [831] Largest Sum of Averages
#
# https://leetcode.com/problems/largest-sum-of-averages/description/
#
# algorithms
# Medium (37.80%)
# Total Accepted:    1.8K
# Total Submissions: 4.9K
# Testcase Example:  '[9,1,2,3,9]\n3'
#
# We partition a row of numbers A into at most K adjacent (non-empty) groups,
# then our score is the sum of the average of each group. What is the largest
# score we can achieve?
# 
# Note that our partition must use every number in A, and that scores are not
# necessarily integers.
# 
# 
# Example:
# Input: 
# A = [9,1,2,3,9]
# K = 3
# Output: 20
# Explanation: 
# The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 +
# (1 + 2 + 3) / 3 + 9 = 20.
# We could have also partitioned A into [9, 1], [2], [3, 9], for example.
# That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
# 
# 
# 
# 
# Note: 
# 
# 
# 1 <= A.length <= 100.
# 1 <= A[i] <= 10000.
# 1 <= K <= A.length.
# Answers within 10^-6 of the correct answer will be accepted as correct.
# 
# 
#
class Solution(object):
    def largestSumOfAverages(self, A, K):
        memo = {}
        def search(n, k):
            if (n, k) in memo: return memo[n, k]
            if k == 1:
                memo[n, k] = sum(A[:n]) / float(n)
                return memo[n, k]
            cur, memo[n, k] = 0, 0
            for i in range(n - 1, 0, -1):
                cur += A[i]
                memo[n, k] = max(memo[n, k], search(i, k - 1) + cur / float(n - i))
            return memo[n, k]
        return search(len(A), K)
