#
# [800] Letter Case Permutation
#
# https://leetcode.com/problems/letter-case-permutation/description/
#
# algorithms
# Easy (52.22%)
# Total Accepted:    4.4K
# Total Submissions: 8.5K
# Testcase Example:  '"a1b2"'
#
# Given a string S, we can transform every letter individually to be lowercase
# or uppercase to create another string.  Return a list of all possible strings
# we could create.
# 
# 
# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
# 
# Input: S = "3z4"
# Output: ["3z4", "3Z4"]
# 
# Input: S = "12345"
# Output: ["12345"]
# 
# 
# Note:
# 
# 
# S will be a string with length at most 12.
# S will consist only of letters or digits.
# 
# 
#
class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        self.backtracking(0, "",S,res)
        return res
    
    def backtracking(self, i, s,S,res):
            if i == len(S):
                res.append(s)
                return
            if not S[i] in "0123456789":
                self.backtracking(i + 1, s + S[i].lower(),S,res)
                self.backtracking(i + 1, s + S[i].upper(),S,res)
            else:
                self.backtracking(i + 1, s + S[i],S,res)
