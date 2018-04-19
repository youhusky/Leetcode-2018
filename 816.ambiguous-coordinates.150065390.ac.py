#
# [834] Ambiguous Coordinates
#
# https://leetcode.com/problems/ambiguous-coordinates/description/
#
# algorithms
# Medium (41.54%)
# Total Accepted:    1.7K
# Total Submissions: 4.1K
# Testcase Example:  '"(123)"'
#
# We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".  Then, we
# removed all commas, decimal points, and spaces, and ended up with the string
# S.  Return a list of strings representing all possibilities for what our
# original coordinates could have been.
# 
# Our original representation never had extraneous zeroes, so we never started
# with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other
# number that can be represented with less digits.  Also, a decimal point
# within a number never occurs without at least one digit occuring before it,
# so we never started with numbers like ".1".
# 
# The final answer list can be returned in any order.  Also note that all
# coordinates in the final answer have exactly one space between them
# (occurring after the comma.)
# 
# 
# Example 1:
# Input: "(123)"
# Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
# 
# 
# 
# Example 2:
# Input: "(00011)"
# Output:  ["(0.001, 1)", "(0, 0.011)"]
# Explanation: 
# 0.0, 00, 0001 or 00.01 are not allowed.
# 
# 
# 
# Example 3:
# Input: "(0123)"
# Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)",
# "(0.12, 3)"]
# 
# 
# 
# Example 4:
# Input: "(100)"
# Output: [(10, 0)]
# Explanation: 
# 1.0 is not allowed.
# 
# 
# 
# 
# Note: 
# 
# 
# 4 <= S.length <= 12.
# S[0] = "(", S[S.length - 1] = ")", and the other elements in S are digits.
# 
# 
# 
#
class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
#         In sub functon f(S)
# if S == “”: return []
# if S == “0”: return [S]
# if S == “0XXX0”: return []
# if S == “0XXX”: return [“0.XXX”]
# if S == “XXX0”: return [S]
# return [S, “X.XXX”, “XX.XX”, “XXX.X”…]
        res = []
        for i in range(2, len(S)-1):
            l = self.check(S[1:i])
            r = self.check(S[i:-1])
            print l,r
            for i in l:
                for j in r:
                    res.append('(' + i + ", " + j + ')')
        return res
                
        
    def check(self, s):
        res = []
        if len(s) == 1:
            res.append(s)
        elif s[0] == '0' and s[-1] == '0':
            return []
        elif s[0] == '0':
            res.append("0." + s[1:])
        elif s[-1] == '0':
            res.append(s)
        else:
            res.append(s)
            for i in range(1,len(s)):
                res.append(s[:i] + '.' + s[i:])
        return res
