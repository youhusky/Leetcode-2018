#
# [804] Rotated Digits
#
# https://leetcode.com/problems/rotated-digits/description/
#
# algorithms
# Easy (51.16%)
# Total Accepted:    2.3K
# Total Submissions: 4.5K
# Testcase Example:  '10'
#
# X is a good number if after rotating each digit individually by 180 degrees,
# we get a valid number that is different from X. A number is valid if each
# digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and
# 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the
# numbers do not rotate to any other number.
# 
# Now given a positive number N, how many numbers X from 1 to N are good?
# 
# 
# Example:
# Input: 10
# Output: 4
# Explanation: 
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after
# rotating.
# 
# 
# 
# Note:
# 
# 
# N  will be in range [1, 10000].
# 
# 
#
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count=0
        for i in range(1, N+1):
            s=str(i)
            flag=1
            for c in s:
                if c=="3" or c=="4" or c=="7":
                    flag=0
                    break
                if c=="2" or c=="5" or c=="6" or c=="9":
                    flag=2
            if flag==2: count+=1
        return count
